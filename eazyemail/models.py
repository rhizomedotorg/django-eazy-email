import json
import markdown

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.db import models
from django.template import Template
from django.template.defaultfilters import slugify
from django.template.loader import render_to_string

from eazyemail.context import EmailContext


class EazyEmail(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    dummy_data = models.TextField(blank=True)
    subject = models.CharField(max_length=100, blank=True)
    text_body = models.TextField(blank=True)
    html_body = models.TextField('HTML body', blank=True)
    template_name = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(EazyEmail, self).save(*args, **kwargs)

    @property
    def dummy_data_dict(self):
        return json.loads(self.dummy_data)

    def get_absolute_url(self):
        return reverse('eazyemail_preview', args=([self.slug]))

    def __unicode__(self):
        return '%s' % self.title

    def render_text_body(self, dictionary={}):
        return Template(self.text_body).render(EmailContext(dictionary))

    def render_html_body(self, dictionary={}):
        return Template(markdown.markdown(self.html_body)).render(EmailContext(dictionary))

    def html_content(self, dictionary={}):
        if not self.template_name:
            return self.render_html_body(dictionary)

        dictionary.update({
            'message_body': self.render_html_body(dictionary),
        })
        return render_to_string(self.template_name, dictionary)

    def send(self, from_email, to, bcc=None, extra_context={}, text_only=False):
        email = EmailMultiAlternatives(self.subject, self.render_text_body(extra_context), from_email, to, bcc)
        if not text_only:
            email.attach_alternative(self.html_content(extra_context), 'text/html')
        email.send(fail_silently=False)
