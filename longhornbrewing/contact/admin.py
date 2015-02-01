from django.contrib import admin
from contact.models import ContactPage

class ContactPageAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(ContactPage, ContactPageAdmin)
