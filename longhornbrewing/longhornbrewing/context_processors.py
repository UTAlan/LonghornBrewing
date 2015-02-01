def contact_info(request):
    from contact.models import ContactPage

    contactinfo = ContactPage.objects.get(id=1)

    return { 'contactinfo': contactinfo }
