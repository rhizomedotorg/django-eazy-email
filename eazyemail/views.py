from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from eazyemail.models import EazyEmail


def preview(request, slug):
    email = get_object_or_404(EazyEmail, slug=slug)
    return HttpResponse(email.html_content(email.dummy_data_dict))
