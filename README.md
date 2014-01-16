django-eazy-email
=================

```bash
pip install -e git+https://github.com/rhizomedotorg/django-eazy-email.git@master#egg=django_eazy_email-dev
```

```python
INSTALLED_APPS (
    ...
    'django_eazy_email',
)

EAZY_EMAIL_CONTEXT_PROCESSORS = (
    'django_eazy_email.context_processors.static',
    'django_eazy_email.context_processors.media',
)
```

```python
url(r'^email/', include('eazyemail.urls')),
```
