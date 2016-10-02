from tests import TestCase
from config import settings
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


class AboutPageTestCase(TestCase):
    def test_title(self):
        content = self.client.get('about/index.html')
        self.assertHeaderTitle(content, 'About Me')
        self.assertTitle(content, 'About')

    def test_website_section(self):
        content = self.client.get('about/index.html')
        section = content.find('section', id='website')
        subtitle = section.find('h2')
        self.assertEqual('About my website', self.get_children(subtitle))

    def test_server_section(self):
        content = self.client.get('about/index.html')
        section = content.find('section', id='server')
        subtitle = section.find('h2')
        self.assertEqual('The Server', self.get_children(subtitle))

    def test_github_card(self):
        content = self.client.get('about/index.html')
        tags = content.find_all('div', class_='github-card')
        self.assertEqual(len(tags), 1)
        tag = tags[0]
        self.assertEqual('medium', tag.attrs['data-theme'])
        self.assertEqual(settings.accounts.github[1], tag.attrs['data-github'])


class Page404TestCase(TestCase):
    def test_title(self):
        content = self.client.get('.404.html')
        self.assertHeaderTitle(content, 'Uh Oh - There\'s nothing here!')
        self.assertTitle(content, '404 - Page not found')

    def test_image(self):
        content = self.client.get('.404.html')
        img = content.find('img')
        self.assertEqual('Cat', img.attrs['alt'])
