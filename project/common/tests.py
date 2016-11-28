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


class DjangoAdminDisabledTestCase(BaseTestCase):
    def test_admin_enabled(self):
        with self.settings(ENABLE_ADMIN=True):
            response = self.client.get('/django-admin/login/', follow=True)
            self.assertEqual(response.status_code, 200)

        with self.settings(DEBUG=True):
            response = self.client.get('/django-admin/login/', follow=True)
            self.assertEqual(response.status_code, 200)

    def test_admin_disabled(self):
        with self.settings(ENABLE_ADMIN=False):
            response = self.client.get('/django-admin/login/', follow=True)
            self.assertEqual(response.status_code, 200)

        with self.settings(DEBUG=False):
            response = self.client.get('/django-admin/login/', follow=True)
            self.assertEqual(response.status_code, 200)
