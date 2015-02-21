from django.contrib import admin
from homepage.models import HomePage, SliderItem

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(HomePage, HomePageAdmin)

class SliderItemAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SliderItem, SliderItemAdmin)
