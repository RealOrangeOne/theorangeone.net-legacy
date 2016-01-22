from django.test import TestCase
from django.core.urlresolvers import reverse
import os.path

PATH = os.path.dirname(os.path.abspath(__file__))

class CustomTemplateTestCase(TestCase):
    def setUp(self):
        self.template = 'pages:index'

    def test_accessable(self):
        response = self.client.get(reverse(self.template))
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(reverse(self.template))
        for item in ['html_title', 'body_class', 'js_redirect']:
            self.assertIn(item, response.context)


class ReverserTestCase(TestCase):
    REVERSER_IDENT = 'reverser:reverser'
    def test_reverser(self):
        response = self.client.post(reverse(self.REVERSER_IDENT), data={'ident': 'pages:index'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.data, reverse('pages:index'))

    def test_invalid_reverser(self):
        response = self.client.post(reverse(self.REVERSER_IDENT), data={'ident': 'pages:i-dont-exist'})
        self.assertEqual(response.status_code, 404)


class MarkdownViewTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('pages:projects', args=['test']))
        self.assertEqual(response.status_code, 200)

    def test_parsing(self):
        response = self.client.get(reverse('pages:projects', args=['test']))
        self.assertContains(response, '<h1>Testing</h1>')

    def test_template_engine(self):
        response = self.client.get(reverse('pages:projects', args=['test']))
        self.assertContains(response, reverse('pages:all-projects'))

    def test_invalid_template(self):
        response = self.client.get(reverse('pages:projects', args=['not-a-project']))
        self.assertEqual(response.status_code, 404)
