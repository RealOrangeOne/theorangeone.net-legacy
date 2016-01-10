from django.test import TestCase
from django.core.urlresolvers import reverse


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
