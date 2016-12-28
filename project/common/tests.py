from wagtail.tests.utils import WagtailPageTests
from .context import SETTINGS_KEYS
from django.conf import settings
from project.home.models import HomePage
from wagtail.wagtailcore.models import Site, Page
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from django.utils.text import slugify
from bs4 import BeautifulSoup


class BaseTestCase(WagtailPageTests):
    client = APIClient()

    def setUp(self):
        super().setUp()

        self.root = self.create_initial_homepage()

    def create_model(self, model, data={}):
        add_url = reverse('wagtailadmin_pages:add', args=[
            model._meta.app_label, model._meta.model_name, self.root.pk
        ])
        data.update({
            'action-publish': 'action-publish',
            'body-count': 1,
            'body-0-deleted': '',
            'body-0-order': 0,
            'body-0-type': 'raw_html',
            'body-0-value': data['body'],
            'slug': slugify(data['title'])
        })
        return self.client.post(add_url, data)

    def create_test_user(self):
        self.user = super().create_test_user()
        return self.user

    def parse_content(self, content):
        return BeautifulSoup(content, 'html.parser')

    def create_initial_homepage(self):
        """
            from https://github.com/wagtail/wagtail/blob/master/wagtail/project_template/home/migrations/0002_create_homepage.py
        """
        Page.objects.filter(id=2).delete()

        # Create a new homepage
        homepage = HomePage.objects.create(
            title="Homepage",
            slug='home',
            path='00010001',
            depth=2,
            numchild=0,
            url_path='/',
        )
        Site.objects.create(hostname='localhost', root_page=homepage, is_default_site=True)
        return homepage


class ContextInjectorTestCase(BaseTestCase):
    def test_has_keys(self):
        response = self.client.get('/')
        for key in SETTINGS_KEYS:
            self.assertIn(key, response.context['settings'])
            self.assertEqual(response.context['settings'][key], getattr(settings, key))


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
