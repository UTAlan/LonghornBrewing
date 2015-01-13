from django.conf.urls import patterns

urlpatterns = patterns('beers.views',
    (r'^$', 'index')
)