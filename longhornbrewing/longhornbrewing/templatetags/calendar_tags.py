from __future__ import unicode_literals

import heapq

from django.template import Library
from django.conf import settings
from django.utils import timezone

from happenings.utils.upcoming import UpcomingEvents
from happenings.models import Event
from happenings.utils.displays import month_display
from happenings.utils.common import (
    get_net_category_tag,
    get_qs,
    clean_year_month,
    now
)

from bs4 import BeautifulSoup

register = Library()
start_day = getattr(settings, "CALENDAR_START_DAY", 0)


@register.simple_tag
def show_my_calendar(req, mini=False):
    net, category, tag = get_net_category_tag(req)
    year = now.year
    month = now.month + net
    year, month, error = clean_year_month(year, month, None)

    prefetch = {'loc': True, 'cncl': True}
    if mini:
        prefetch['loc'] = False  # locations aren't displayed on mini calendar

    all_month_events = list(Event.objects.all_month_events(
        year, month, category, tag, **prefetch
    ))
    all_month_events.sort(key=lambda x: x.l_start_date.hour)
    qs = req.META['QUERY_STRING']
    if qs:  # get any querystrings that are not next/prev
        qs = get_qs(qs)
    soup = BeautifulSoup(month_display(year, month, all_month_events, start_day, net, qs, mini=mini))

    # Remove links from Dates
    for tag in soup.select('a[href^="/calendar/"]'):
        if not tag.has_attr('class'):
            tag.unwrap()

    # Fix formatting for Events
    for tag in soup.select('div.calendar-event'):
        event_id = tag.parent.get("href")[16:-1]

        idx = 0
        while idx < len(all_month_events) and str(all_month_events[idx].id) != event_id:
            idx += 1
        if idx == len(all_month_events):
            idx = 0

        event_title = soup.new_tag('div')
        event_title['class'] = ['event_title', 'hidden', 'event_id_' + str(all_month_events[idx].id)]
        event_title.string = all_month_events[idx].title
        tag.insert(0, event_title)

        event_date = soup.new_tag('div')
        event_date['class'] = ['event_date', 'hidden']
        event_date.string = all_month_events[idx].start_date.strftime('%B %d, %Y')
        tag.insert(1, event_date)

        event_description = soup.new_tag('div')
        event_description['class'] = ['event_description', 'hidden']
        event_description.string = all_month_events[idx].description
        tag.insert(2, event_description)

    return soup.prettify()
