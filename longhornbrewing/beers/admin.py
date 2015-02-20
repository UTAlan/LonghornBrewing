from django.contrib import admin
from beers.models import Beer, OurBeer

class BeerAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Beer, BeerAdmin)

class OurBeerAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(OurBeer, OurBeerAdmin)
