from django.conf.urls import patterns

urlpatterns = patterns('findus.views',
    (r'^$', 'index')
)
