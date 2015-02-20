from django.contrib import admin
from store.models import Product, Store

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price',)

admin.site.register(Product, ProductAdmin)

class StoreAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Store, StoreAdmin)
