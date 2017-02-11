from tests import TestCase
from config import social as social_settings
import pelicanconf as settings
import os.path


class HomepageTestCase(TestCase):
    def test_about_section(self):
        content = self.client.get('index.html')
        about = content.find('section', id='about')
        self.assertIsNotNone(about)
        about_content = about.find('p')
        self.assertNotEqual(self.get_children(about_content), '')
        about_link = about.find('a')
        self.assertTrue(self.client.exists(about_link.attrs['href']))

    def test_blog_links(self):
        content = self.client.get('index.html')
        blog = content.find('section', id='blog')
        blog_link = blog.find('a', class_='btn')
        self.assertTrue(self.client.exists(blog_link.attrs['href']))
        blogs = blog.find_all('div', class_="col-xs-12")
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

    def test_navbar(self):
        content = self.client.get('index.html')
        links = content.find('ul', class_='navbar-nav').find_all('a')
        self.assertEqual(len(links), 5)
        for link in links:
            self.assertIn('page-scroll', link.attrs['class'])
            element = self.get_children(link)
            self.assertEqual(link.attrs['href'], '#' + element.lower())


class AboutPageTestCase(TestCase):
    def test_title(self):
        content = self.client.get('about/index.html')
        self.assertHeaderTitle(content, 'About')
        self.assertTitle(content, 'About')

    def test_github_card(self):
        content = self.client.get('about/index.html')
        tags = content.find_all('div', class_='github-card')
        self.assertEqual(len(tags), 1)
        tag = tags[0]
        self.assertEqual('medium', tag.attrs['data-theme'])
        self.assertEqual(social_settings['accounts']['github'][1], tag.attrs['data-github'])

    def test_accounts(self):
        content = self.client.get('about/index.html')
        accounts = content.find_all('div', class_='account')
        defined_accounts = [s for k, s in settings.ACCOUNTS.items()]
        self.assertEqual(len(accounts), len(defined_accounts))
        site_names = [s['site'] for s in defined_accounts]
        urls = [s['url'] for s in defined_accounts]
        icons = [s['icon'] for s in defined_accounts]
        for account in accounts:
            self.assertIn(account.find('a').attrs['href'], urls)
            self.assertIn(account.find('i').attrs['class'][-1], icons)
            self.assertIn(self.get_children(account.find('h3')), site_names)


class ContactPageTestCase(TestCase):
    def test_title(self):
        content = self.client.get('contact/')
        self.assertHeaderTitle(content, 'Contact Me')
        self.assertTitle(content, 'Contact Me')

    def test_contact_links(self):
        content = self.client.get('contact/')
        links = content.find_all('section')[2].find_all('a')
        self.assertEqual(links[1].attrs['href'], settings.ACCOUNTS['twitter']['url'])
        decoded_value = ''.join([chr(int(c)) for c in links[0].attrs['data-value'].split(' ')])
        self.assertEqual(decoded_value, settings.CONTACT_EMAIL)


class Page404TestCase(TestCase):
    def test_title(self):
        content = self.client.get('.404.html')
        self.assertHeaderTitle(content, 'Uh Oh - There\'s nothing here!')
        self.assertTitle(content, '404 - Page not found')

    def test_image(self):
        content = self.client.get('.404.html')
        img = content.find('img')
        self.assertEqual('Cat', img.attrs['alt'])
