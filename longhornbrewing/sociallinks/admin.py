from django.contrib import admin
from sociallinks.models import SocialLink

class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SocialLink, SocialLinkAdmin)
