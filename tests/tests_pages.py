from tests import TestCase
import os.path


class HomepageTestCase(TestCase):
    def test_blog_links(self):
        content = self.client.get('index.html')
        blogs = content.find('section', id='blog').find_all('div', class_="col-xs-12")
        self.assertTrue(len(blogs) <= 4)
        for post in blogs:
            url = os.path.join(post.find('a').attrs['href'], 'index.html')
            self.assertTrue(self.client.exists(url))

    def test_projects(self):
        content = self.client.get('index.html')
        projects = content.find('section', id='projects').find_all('a', class_='portfolio-box')
        for project in projects:
            url = os.path.join(project.attrs['href'], 'index.html')
            self.assertTrue(self.client.exists(url))
