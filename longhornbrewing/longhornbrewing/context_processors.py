def contact_info(request):
    from contact.models import Contact
    from eventspage.models import Event
    from sociallinks.models import SocialLink
    from bgs.models import Background
    from pagestyle.models import PageStyle
    from findus.models import FindUs
    from store.models import Store

    contactinfo = Contact.objects.get(id=1)
    eventspage = Event.objects.get(id=1)
    sociallinks = SocialLink.objects.filter(public=True).order_by('order')
    bg_header = Background.objects.get(id=1)
    bg_body = Background.objects.get(id=2)
    page_style = PageStyle.objects.filter(active=True)
    find_us = FindUs.objects.get(id=1)
    store = Store.objects.get(id=1)

    return { 'contactinfo': contactinfo, 'eventspage': eventspage, 'sociallinks': sociallinks, 'bg_header': bg_header, 'bg_body': bg_body, 'page_style': page_style[0], 'find_us': find_us, 'store': store }
