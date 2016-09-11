from tests.TestWrapper import TestCase
from bs4 import BeautifulSoup


class TestClientTestCase(TestCase):
    def test_client_fails(self):
        with self.assertRaises(FileNotFoundError):
            self.client.get('foo.bar')

    def test_client_gets_data(self):
        content = self.client.get('index.html')
        self.assertIsInstance(content, BeautifulSoup)

    def test_file_exists(self):
        self.assertTrue(self.client.exists('index.html'))

    def test_file_doesnt_exist(self):
        self.assertFalse(self.client.exists('foo.bar'))
