def contact_info(request):
    from contact.models import Contact
    from eventspage.models import Event
    from sociallinks.models import SocialLink
    from bgs.models import Background

    contactinfo = Contact.objects.get(id=1)
    eventspage = Event.objects.get(id=1)
    sociallinks = SocialLink.objects.filter(public=True).order_by('order')
    bg_header = Background.objects.get(id=1)
    bg_body = Background.objects.get(id=2)

    return { 'contactinfo': contactinfo, 'eventspage': eventspage, 'sociallinks': sociallinks, 'bg_header': bg_header, 'bg_body': bg_body }
