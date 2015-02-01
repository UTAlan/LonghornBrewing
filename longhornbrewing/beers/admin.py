from django.contrib import admin
from beers.models import Beer

class BeerAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Beer, BeerAdmin)
