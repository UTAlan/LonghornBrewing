from django.contrib import admin
from homepage.models import HomePage

class HomePageAdmin(admin.ModelAdmin):
    #fields = ('title', 'slogan', 'content_left',)
    list_display = ('title',)
    
    #class Media:
    #    js = ("http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js","http://www.zurb.com/javascripts/plugins/jquery.textchange.min.js",)

admin.site.register(HomePage, HomePageAdmin)
