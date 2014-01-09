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

# django-eazy-email
EAZY_EMAIL_CONTEXT_PROCESSORS = (
    'django_eazy_email.context_processors.static',
    'django_eazy_email.context_processors.media',
)
```
