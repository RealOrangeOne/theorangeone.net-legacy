from django.test import TestCase
from django.conf import settings
import os.path
from glob import glob


class PagesTestCase(TestCase):
    def setUp(self):
        directories = glob(os.path.join(settings.BASE_DIR, 'templates') + '/**/*.*')
        self.urls = []
        for directory in directories:
            if 'email' in directory or 'blog' in directory:
                continue
            self.urls.append(directory.replace(os.path.join(settings.BASE_DIR, 'templates'), '').split('.')[0].replace('index', ''))

    def test_pages_accessable(self):
        for path in self.urls:
            response = self.client.get(path)
            self.assertEqual(response.status_code, 200)
