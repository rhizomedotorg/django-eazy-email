from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from eazyemail.models import EazyEmail


def preview(request, slug):
    email = get_object_or_404(EazyEmail, slug=slug)

    if email.html_body:
        return HttpResponse(email.html_content(email.dummy_data_dict))

    content = email.render_text_body(email.dummy_data_dict)
    return HttpResponse(content, content_type='text/plain')
