from django.conf.urls import patterns, url


urlpatterns = patterns('eazyemail.views',
    url(r'^(?P<slug>\w+)/$', 'preview', name='eazyemail_preview'),
)
