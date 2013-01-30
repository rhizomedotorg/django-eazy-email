from django.conf.urls.defaults import patterns
from django.contrib import admin
from django_eazy_email.models import EazyEmail
from django_eazy_email.views import preview


class EazyEmailAdmin(admin.ModelAdmin):
    def get_urls(self):
        urls = super(EazyEmailAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^(?P<object_id>.+|\d+)/preview/$', preview)
        )
        return my_urls + urls

admin.site.register(EazyEmail, EazyEmailAdmin)