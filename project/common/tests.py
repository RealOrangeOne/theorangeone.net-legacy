from wagtail.tests.utils import WagtailPageTests
from .context import SETTINGS_KEYS
from django.conf import settings
from project.home.models import HomePage
from wagtail.wagtailcore.models import Site, Page
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient
from django.utils.text import slugify
from bs4 import BeautifulSoup


class BaseTestCase(WagtailPageTests):
    USERNAME = 'test_user'
    EMAIL = 'test@example.com'
    PASSWORD = 'test'

    def setUp(self):
        super().setUp()

        self.client = APIClient()
        self.root = self.create_initial_homepage()
        self.user = User.objects.create_superuser(
            self.USERNAME,
            self.EMAIL,
            self.PASSWORD
        )
        self.client.login(
            username=self.USERNAME,
            password=self.PASSWORD
        )

    def create_model(self, model, data={}):
        add_url = reverse('wagtailadmin_pages:add', args=[
            model._meta.app_label, model._meta.model_name, self.root.pk
        ])
        data['action-publish'] = 'action-publish'
        data['body-count'] = 1
        data['body-0-deleted'] = ''
        data['body-0-order'] = 0
        data['body-0-type'] = 'raw_html'
        data['body-0-value'] = data['body']
        data['slug'] = slugify(data['title'])
        return self.client.post(add_url, data)

    def parse_content(self, content):
        parsed_content = BeautifulSoup(content, 'html.parser')
        for tag in parsed_content(["noscript"]):  # Remove noscript tags
            tag.extract()
        return parsed_content

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
