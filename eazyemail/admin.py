from django.contrib import admin
from eazyemail.models import EazyEmail


class EazyEmailAdmin(admin.ModelAdmin):
    pass

admin.site.register(EazyEmail, EazyEmailAdmin)
