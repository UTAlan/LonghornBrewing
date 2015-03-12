def contact_info(request):
    from contact.models import Contact
    from eventspage.models import Event
    from sociallinks.models import SocialLink

    contactinfo = Contact.objects.get(id=1)
    eventspage = Event.objects.get(id=1)
    sociallinks = SocialLink.objects.filter(public=True).order_by('order')

    return { 'contactinfo': contactinfo, 'eventspage': eventspage, 'sociallinks': sociallinks }
