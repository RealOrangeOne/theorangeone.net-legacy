from django.conf import settings


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


def settings_injector(request=None):
    injected_settings = {}
    for setting in SETTINGS_KEYS:
        injected_settings[setting] = getattr(settings, setting)
    return {'django_settings': injected_settings}
