from django.conf.urls.defaults import patterns
from django.contrib import admin
from eazyemail.models import EazyEmail
from eazyemail.views import preview


class EazyEmailAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(EazyEmailAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^(?P<object_id>.+|\d+)/preview/$', preview)
        )
        return my_urls + urls

admin.site.register(EazyEmail, EazyEmailAdmin)
