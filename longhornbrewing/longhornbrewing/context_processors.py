def contact_info(request):
    from contact.models import Contact
    from eventspage.models import Event
    from sociallinks.models import SocialLink
    from bgs.models import Background
    from pagestyle.models import PageStyle
    from findus.models import FindUs
    from store.models import Store

    contactinfo = Contact.objects.filter(id=1)
    eventspage = Event.objects.filter(id=1)
    sociallinks = SocialLink.objects.filter(public=True).order_by('order')
    bg_header = Background.objects.filter(id=1)
    bg_body = Background.objects.filter(id=2)
    page_style = PageStyle.objects.filter(active=True)
    find_us = FindUs.objects.filter(id=1)
    store = Store.objects.filter(id=1)

    return { 'contactinfo': contactinfo[0], 'eventspage': eventspage[0], 'sociallinks': sociallinks, 'bg_header': bg_header[0], 'bg_body': bg_body[0], 'page_style': page_style[0], 'find_us': find_us[0], 'store': store[0] }
