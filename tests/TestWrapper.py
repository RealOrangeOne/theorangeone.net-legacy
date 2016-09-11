import unittest
import os.path
from bs4 import BeautifulSoup


class TestClient:
    output_path = os.path.realpath('./output')

    def get(self, path):
        file_path = self.build_path(path)
        content = "".join(open(file_path).readlines())
        if path.endswith('html'):
            content = BeautifulSoup(content, 'html.parser')
        return content

    def build_path(self, path):
        if path.startswith('/'):
            path = path[1:]
        return os.path.join(self.output_path, path)

    def exists(self, path):
        try:
            open(self.build_path(path)).close()
            return True
        except FileNotFoundError:
            return False


class TestCase(unittest.TestCase):
    client = TestClient()

    def assertTitle(self, content, title):
        self.assertIn(title, content.title.string)
