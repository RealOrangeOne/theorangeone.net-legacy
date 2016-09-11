from tests.TestWrapper import TestCase
import os.path


class HomepageTestCase(TestCase):
    def test_blog_links(self):
        content = self.client.get('index.html')
        blogs = content.find('section', id='blog').find_all('div', class_="col-xs-12")
        self.assertTrue(len(blogs) <= 4)
        for post in content.find('section', id='blog').find_all('div', class_="col-xs-12"):
            url = os.path.join(post.find('a').attrs['href'], 'index.html')
            self.assertTrue(self.client.exists(url))
