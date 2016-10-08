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
            for script in content(["noscript"]):  # Remove extra tags
                script.extract()
        return content

    def build_path(self, path):
        if path.startswith('/'):
            path = path[1:]
        return os.path.join(self.output_path, path)

    def exists(self, path):
        try:
            with open(self.build_path(path)):
                return True
        except FileNotFoundError:
            return False


class TestCase(unittest.TestCase):
    client = TestClient()

    def get_children(self, content):
        return str(list(content.children)[0])

    def assertTitle(self, content, title):
        self.assertIn(title, content.title.string)

    def assertHeaderTitle(self, content, title):
        header_title = content.find('h1', class_="section-heading")
        self.assertIn(title, self.get_children(header_title))
