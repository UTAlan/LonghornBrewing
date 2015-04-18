from django.http import Http404
from django.shortcuts import render
from django.conf import settings

from homepage.models import HomePage, SliderItem

from calendar import month_name

from happenings.utils.upcoming import UpcomingEvents
from happenings.models import Event
from happenings.utils.displays import month_display
from happenings.utils import common as c
from happenings.utils.common import (
    get_net_category_tag,
    get_qs,
    clean_year_month,
    now
)
from happenings.views import GenericEventView

from bs4 import BeautifulSoup


def index(request):
    info = {}

    info['homepage'] = HomePage.objects.get(id=1)
    info['slideritems'] = SliderItem.objects.filter(active=True).order_by('order').order_by('name')

    return render(request, 'index.html', { 'info': info })

class EventMonthView(GenericEventView):
    template_name = 'happenings/event_month_list.html'

    def get_year_and_month(self, net, qs, **kwargs):
        """
        Get the year and month. First tries from kwargs, then from
        querystrings. If none, or if cal_ignore qs is specified,
        sets year and month to this year and this month.
        """
        year = c.now.year
        month = c.now.month + net
        month_orig = None

        if 'cal_ignore=true' not in qs:
            if 'year' and 'month' in self.kwargs:  # try kwargs
                year, month_orig = map(
                    int, (self.kwargs['year'], self.kwargs['month'])
                )
                month = month_orig + net
            else:
                try:  # try querystring
                    year = int(self.request.GET['cal_year'])
                    month_orig = int(self.request.GET['cal_month'])
                    month = month_orig + net
                except Exception:
                    pass
        # return the year and month, and any errors that may have occurred do
        # to an invalid month/year being given.
        return c.clean_year_month(year, month, month_orig)

    def get_context_data(self, **kwargs):
        context = super(EventMonthView, self).get_context_data(**kwargs)

        qs = self.request.META['QUERY_STRING']

        year, month, error = self.get_year_and_month(self.net, qs)

        mini = True if 'cal_mini=true' in qs else False

        # get any querystrings that are not next/prev/year/month
        if qs:
            qs = c.get_qs(qs)

        # add a dict containing the year, month, and month name to the context
        current = dict(
            year=year, month_num=month, month=month_name[month][:3]
        )
        context['current'] = current

        context['month_and_year'] = "%(month)s, %(year)d" % (
            {'month': month_name[month], 'year': year}
        )

        if error:  # send any year/month errors
            context['cal_error'] = error

        # List enables sorting. As far as I can tell, .order_by() can't be used
        # here because we need it ordered by l_start_date.hour (simply ordering
        # by start_date won't work). The only alternative I've found is to use
        # extra(), but this would likely require different statements for
        # different databases...
        all_month_events = list(Event.objects.all_month_events(
            year, month, self.category, self.tag, loc=True, cncl=True
        ))

        all_month_events.sort(key=lambda x: (x.l_start_date.year, x.l_start_date.month, x.l_start_date.day))

        start_day = getattr(settings, "CALENDAR_START_DAY", 0)
        soup = BeautifulSoup(month_display(year, month, all_month_events, start_day, self.net, qs, mini))

        # Remove links from Dates
        for tag in soup.select('a[href^="/calendar/"]'):
            if not tag.has_attr('class'):
                tag.unwrap()

        # Fix formatting for Events
        for ev in all_month_events:
            tag = soup.find(attrs={ "title": ev.title })

            if tag:
                event_title = soup.new_tag('div')
                event_title['class'] = ['event_title', 'hidden']
                event_title.string = ev.title
                tag.insert(0, event_title)

                event_date = soup.new_tag('div')
                event_date['class'] = ['event_date', 'hidden']
                event_date.string = ev.start_date.strftime('%B %d, %Y')
                tag.insert(1, event_date)

                event_description = soup.new_tag('div')
                event_description['class'] = ['event_description', 'hidden']
                event_description.string = ev.description
                tag.insert(2, event_description)

        '''
        idx = len(all_month_events) - 1
        for tag in soup.select('div.calendar-event'):
            if incr_set == False and all_month_events[idx].title != tag.title:
                incr = True
                idx = 0

            if incr_set == False:
                incr_set = True

            event_title = soup.new_tag('div')
            event_title['class'] = ['event_title', 'hidden']
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

            test = soup.new_tag('div')
            test['class'] = ['event_test', 'hidden']
            test.string = str(len(all_month_events))
            tag.insert(3, test)

            if incr == True:
                idx += 1
            else:
                idx -= 1
        '''

        context['calendar'] = soup.prettify()

        context['show_events'] = False
        if getattr(settings, "CALENDAR_SHOW_LIST", False):
            context['show_events'] = True
            context['events'] = c.order_events(all_month_events, d=True) \
                if self.request.is_ajax() else c.order_events(all_month_events)

        return context

def custom_404(request):
    return render_to_response('404.html')
