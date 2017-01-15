from tests import TestCase
from bs4 import BeautifulSoup
import pelicanconf as settings
from config import social as social_settings
from unittest import skipIf
from os import environ


class CorePagesTestCase(TestCase):
    def test_has_index(self):
        content = self.client.get('index.html')
        self.assertTitle(content, 'Homepage')

    def test_has_robots(self):
        content = self.client.get('robots.txt')
        self.assertIn('Allow: /', content)

    def test_has_sitemap(self):
        content = self.client.get('sitemap.xml')
        self.assertIn(settings.SITEURL, content)

    def test_has_atom_feed(self):
        content = self.client.get('feed.atom')
        self.assertIn(settings.SITEURL, content)

    def test_has_404_page(self):
        content = self.client.get('.404.html')
        self.assertTitle(content, '404')


class CommonPagesTestCase(TestCase):
    def test_has_scripts(self):
        content = self.client.get('index.html')
        for script in content.find_all('script'):
            if script.attrs.get('id') == 'piwik':
                continue
            self.assertTrue(self.client.exists(script.attrs['src']))

    def test_has_stylesheet(self):
        content = self.client.get('index.html')
        for script in content.find_all('link', rel='stylesheet'):
            self.assertTrue(self.client.exists(script.attrs['href']))

    def test_has_link_icons(self):
        content = self.client.get('index.html')
        for script in content.find_all('link', rel='icon'):
            self.assertTrue(self.client.exists(script.attrs['href']))
        for script in content.find_all('link', rel='apple-touch-icon-precomposed'):
            self.assertTrue(self.client.exists(script.attrs['href']))

    def test_footer_links(self):
        content = self.client.get('index.html')
        footer = content.footer
        for link in footer.find('p', class_="social").find_all('a'):
            self.assertIn(link.attrs['alt'], social_settings['footer_accounts'])
            self.assertIn("fa fa-", str(list(link.children)[0]))

    def test_navbar_links(self):
        content = self.client.get('.404.html')  # a page that isnt home
        links = content.find('ul', class_='navbar-nav').find_all('a')
        self.assertEqual(len(links), 5)
        for link in links:
            element = self.get_children(link)
            self.assertEqual(link.attrs['href'], '/{}/'.format(element.lower()))
            self.assertTrue(self.client.exists(link.attrs['href']))

    def test_navbar_index_link(self):
        content = self.client.get('.404.html')  # a page that isnt home
        link = content.find('a', class_='navbar-brand')
        self.assertTrue(self.client.exists(link.attrs['href']))
        self.assertSamePath(link.attrs['href'], '/')
        self.assertEqual(self.get_children(link), settings.SITENAME)

    @skipIf(not environ.get('BUILD_PRODUCTION', False), 'Not building production')
    def test_has_analytics(self):
        content = self.client.get('index.html', False)
        piwik_script_tag = content.find('script', id='piwik')
        self.assertNotEqual(piwik_script_tag, None)
        piwik_script = self.get_children(piwik_script_tag)
        self.assertIn('piwik.js', piwik_script)
        self.assertIn(str(settings.PIWIK['site_id']), piwik_script)
        piwik_img = content.find('noscript', id='piwik').find('img')
        self.assertIn(settings.PIWIK['url'], piwik_img.attrs['src'])
        self.assertIn(str(settings.PIWIK['site_id']), piwik_img.attrs['src'])


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
