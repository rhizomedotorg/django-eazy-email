from django.conf import settings

def static():
    return {'STATIC_URL': settings.STATIC_URL}

def media():
    return {'MEDIA_URL': settings.MEDIA_URL}