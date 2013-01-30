from django.http import Http404, HttpResponse
from django_eazy_email.models import EazyEmail


def preview(request, object_id, template_name=None, extra_context={}):
    try:
        ez_email= EazyEmail.objects.get(pk=object_id)
    except EazyEmail.DoesNotExist:
        raise Http404   

    return HttpResponse(ez_email.html_content(template_name, extra_context))
