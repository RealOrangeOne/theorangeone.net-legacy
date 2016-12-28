from django.conf import settings
from .models import SocialMediaSettings


SETTINGS_KEYS = [
    'SITE_URL',
    'BASE_URL',
    'STATIC_URL',
    'MEDIA_URL',
    'LANGUAGE_CODE',
    'TIME_ZONE',
    'ALLOWED_HOSTS',
    'WAGTAIL_SITE_NAME'
]


def settings_injector(request):
    django_settings = {}
    for setting in SETTINGS_KEYS:
        django_settings[setting] = getattr(settings, setting)
    django_settings.update({
        'social': SocialMediaSettings.for_site(request.site)
    })
    return {'settings': django_settings}
