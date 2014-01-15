from django.conf.urls.defaults import patterns, url

from eazyemail.views import preview

urlpatterns = patterns('',
    url(r'^preview/(?P<slug>[-\w]+)/$', preview, name='eazyemail_preview'),
)

