from wagtail.tests.utils import WagtailPageTests
from .context import SETTINGS_KEYS
from django.conf import settings


class BaseTestCase(WagtailPageTests):
    pass


class ContextInjectorTestCase(BaseTestCase):
    def test_has_keys(self):
        response = self.client.get('/')
        for key in SETTINGS_KEYS:
            self.assertIn(key, response.context['django_settings'])
            self.assertEqual(response.context['django_settings'][key], getattr(settings, key))
