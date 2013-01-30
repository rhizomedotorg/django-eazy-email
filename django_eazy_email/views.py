from django.http import Http404, HttpResponse
from django_eazy_email.models import EazyEmail

preview(email_title, template_name=None, text_only=False, extra_context={}):
	try:
		email = EazyEmail.objects.get(title=email_title)
	except EazyEmail.DoesNotExist:
		raise Http404	

	if text_only:
		return HttpResponse(email.render_text_body(extra_context))
	elif template_name:
		return HttpResponse(email.html_message(template_name, extra_context))
	else:
		return HttpResponse(email.render_html_body(extra_context))
