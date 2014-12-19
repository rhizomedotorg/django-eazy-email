try:
    from django.conf.urls import patterns, url
except ImportError:  # deprecated since Django 1.4
    from django.conf.urls.defaults import patterns, url  # noqa

from eazyemail.views import preview

urlpatterns = patterns('',
    url(r'^preview/(?P<slug>[-\w]+)/$', preview, name='eazyemail_preview'),
)

