from django.contrib import admin
from findus.models import FindUs

class FindUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(FindUs, FindUsAdmin)
