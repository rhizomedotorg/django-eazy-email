from django.contrib import admin
from eazyemail.models import EazyEmail


class EazyEmailAdmin(admin.ModelAdmin):
    exclude = ('slug',)

admin.site.register(EazyEmail, EazyEmailAdmin)
