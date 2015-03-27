from django.contrib import admin
from pagestyle.models import PageStyle

class PageStyleAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(PageStyle, PageStyleAdmin)
