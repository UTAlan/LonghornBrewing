from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'longhornbrewing.views.index', name='home'),
    url(r'^tweets$', 'longhornbrewing.tweets.index', name='tweets'),

    url(r'^beers/', include('beers.urls', namespace='beers')),
    url(r'^events/month/shift/$', views.EventMonthView.as_view(), name='month_shift'),
    url(r'^events/', include('happenings.urls', namespace='events')),
    url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^store/', include('store.urls', namespace='store')),
    url(r'^find-our-beer/', include('findus.urls', namespace='findus')),
    url(r'^contact/', include('contact.urls', namespace='contact')),

    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.MEDIA_ROOT }),
)

urlpatterns += patterns('django.contrib.staticfiles.views',
    url(r'^(?:googlef5c8055e27343afa.html)?$', 'serve', kwargs={'path': 'googlef5c8055e27343afa.html'}),
)

urlpatterns += staticfiles_urlpatterns()
