from django.conf.urls import patterns

urlpatterns = patterns('store.views',
    (r'^$', 'index')
)