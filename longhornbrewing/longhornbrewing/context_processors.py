def contact_info(request):
    from contact.models import Contact
    from eventspage.models import Event

    contactinfo = Contact.objects.get(id=1)
    eventspage = Event.objects.get(id=1)

    return { 'contactinfo': contactinfo, 'eventspage': eventspage }
