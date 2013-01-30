from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db import models
from django.template import Template
from django.template.loader import render_to_string

from django_eazy_email.context import EmailContext


class EazyEmail(models.Model):
    title = models.SlugField(max_length=100)
    description = models.TextField()
    subject = models.CharField(max_length=100)
    text_body = models.TextField()
    html_body = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

    def render_text_body(self, dictionary):
        return Template(self.text_body).render(EmailContext(dictionary))

    def render_html_body(self, dictionary):
        return Template(self.html_body).render(EmailContext(dictionary))

    def html_message(self, template_name, dictionary):
        dictionary.update({
            'message_body': self.render_html_body(dictionary),
        })
        return render_to_string(template_name, dictionary)

    def send_as_html(self, from_email, to, bcc=None, template_name='django_eazy_email/templates/html_base.html' dictionary={}):
        multi_email = EmailMultiAlternatives(self.subject, self.render_text_body(dictionary), from_email, to, bcc)
        multi_email.attach_alternative(self.html_message(template_name, dictionary), 'text/html')
        multi_email.send(fail_silently=False)

    def send_as_text(self, from_email=None, to=None, bcc=None, dictionary={}):
        text_email = EmailMessage(self.subject, self.render_text_body(dictionary), from_email, to, bcc)
        text_email.send(fail_silently=False)