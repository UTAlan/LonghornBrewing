from django.contrib import admin
from bgs.models import Background

class BackgroundAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Background, BackgroundAdmin)
