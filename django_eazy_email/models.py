from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db import models
from django.template import Template
from django.template.loader import render_to_string

from django_eazy_email.context import EmailContext


class EazyEmail(models.Model):
    title = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    subject = models.CharField(max_length=100, blank=True)
    text_body = models.TextField(blank=True)
    html_body = models.TextField(blank=True)

    def __unicode__(self):
        return '%s' % self.title

    def render_text_body(self, dictionary={}):
        return Template(self.text_body).render(EmailContext(dictionary))

    def render_html_body(self, dictionary={}):
        return Template(self.html_body).render(EmailContext(dictionary))

    def html_content(self, template_name=None, dictionary={}):
        if not template_name:
            return self.render_html_body(dictionary)

        dictionary.update({
            'message_body': self.render_html_body(dictionary),
        })
        return render_to_string(template_name, dictionary)

    def send(self, from_email, to, bcc=None, template_name=None, extra_context={}, text_only=False):
        email = EmailMultiAlternatives(self.subject, self.render_text_body(dictionary), from_email, to, bcc)
        if not text_only:
            email.attach_alternative(self.html_content(template_name, dictionary), 'text/html')
        email.send(fail_silently=False)
