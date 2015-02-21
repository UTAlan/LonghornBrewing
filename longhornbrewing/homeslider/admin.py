from django.contrib import admin
from homeslider.models import SliderItem

class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SliderItem, SliderItemAdmin)
