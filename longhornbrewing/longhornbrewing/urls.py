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
    url(r'^(?:sitemap.xml)?$', 'serve', kwargs={'path': 'sitemap.xml'}),
    url(r'^(?:robots.txt)?$', 'serve', kwargs={'path': 'robots.txt'}),
    url(r'^(?:apple-touch-icon-57x57.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-57x57.png'}),
    url(r'^(?:apple-touch-icon-60x60.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-60x60.png'}),
    url(r'^(?:apple-touch-icon-72x72.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-72x72.png'}),
    url(r'^(?:apple-touch-icon-76x76.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-76x76.png'}),
    url(r'^(?:apple-touch-icon-114x114.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-114x114.png'}),
    url(r'^(?:apple-touch-icon-120x120.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-120x120.png'}),
    url(r'^(?:apple-touch-icon-144x144.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-144x144.png'}),
    url(r'^(?:apple-touch-icon-152x152.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-152x152.png'}),
    url(r'^(?:apple-touch-icon-180x180.png)?$', 'serve', kwargs={'path': 'apple-touch-icon-180x180.png'}),
    url(r'^(?:favicon-32x32.png)?$', 'serve', kwargs={'path': 'favicon-32x32.png'}),
    url(r'^(?:android-chrome-192x192.png)?$', 'serve', kwargs={'path': 'android-chrome-192x192.png'}),
    url(r'^(?:favicon-96x96.png)?$', 'serve', kwargs={'path': 'favicon-96x96.png'}),
    url(r'^(?:favicon-16x16.png)?$', 'serve', kwargs={'path': 'favicon-16x16.png'}),
    url(r'^(?:manifest.json)?$', 'serve', kwargs={'path': 'manifest.json'}),
    url(r'^(?:mstile-144x144.png)?$', 'serve', kwargs={'path': 'mstile-144x144.png'}),
)

urlpatterns += staticfiles_urlpatterns()

handler404 = 'app.views.custom_404'
