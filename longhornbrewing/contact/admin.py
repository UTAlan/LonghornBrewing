from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Contact, ContactAdmin)
