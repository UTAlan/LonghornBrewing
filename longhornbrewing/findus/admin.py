from django.contrib import admin
from findus.models import FindUs, Location

class FindUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(FindUs, FindUsAdmin)
admin.site.register(Location, LocationAdmin)
