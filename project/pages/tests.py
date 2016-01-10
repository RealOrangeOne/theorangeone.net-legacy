from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)


class AboutWebsiteTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('pages:about-website'))
        self.assertEqual(response.status_code, 200)


class AboutIndexTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('pages:about'))
        self.assertEqual(response.status_code, 200)


class Custom404TestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 404)


class NoJavascriptTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('no-js'))
        self.assertEqual(response.status_code, 200)
