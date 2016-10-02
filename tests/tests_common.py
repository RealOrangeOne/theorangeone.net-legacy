from tests import TestCase
from config import settings, DotDictionary


class CorePagesTestCase(TestCase):
    def test_has_index(self):
        content = self.client.get('index.html')
        self.assertTitle(content, 'Homepage')

    def test_has_robots(self):
        content = self.client.get('robots.txt')
        self.assertIn('Allow: /', content)

    def test_has_sitemap(self):
        content = self.client.get('sitemap.xml')
        self.assertIn(settings.url, content)

    def test_has_atom_feed(self):
        content = self.client.get('feed.atom')
        self.assertIn(settings.url, content)

    def test_has_404_page(self):
        content = self.client.get('.404.html')
        self.assertTitle(content, '404')

    def test_has_scripts(self):
        content = self.client.get('index.html')
        for script in content.find_all('script'):
            self.client.exists(script.attrs['src'])

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
            self.assertIn(link.attrs['alt'], settings.footer_accounts)
            self.assertIn("fa fa-", str(list(link.children)[0]))


class DotDictionaryTestCase(TestCase):
    def setUp(self):
        self.test_dict = DotDictionary({
            'foo': 'bar',
            'bar': {
                'foo': 'bar'
            }
        })

    def test_returns_value(self):
        self.assertEqual(self.test_dict.foo, 'bar')

    def test_returns_self_on_dict(self):
        self.assertEqual(self.test_dict.bar, {
            'foo': 'bar'
        })
        self.assertIsInstance(self.test_dict.bar, DotDictionary)

    def test_set(self):
        self.test_dict.baz = 'foo'
        self.assertEqual(self.test_dict, {
            'foo': 'bar',
            'baz': 'foo',
            'bar': {
                'foo': 'bar'
            }
        })

    def test_delete(self):
        del self.test_dict.bar
        with self.assertRaises(KeyError):
            print(self.test_dict.bar)
        self.assertEqual(self.test_dict, {
            'foo': 'bar'
        })


class WrappedSettingTestCase(TestCase):
    def test_has_data(self):
        self.assertIsInstance(settings.settings, dict)
        self.assertTrue(len(settings.settings))

    def test_returns_values(self):
        self.assertEqual(settings.language, 'en')
        self.assertEqual(settings.timezone, 'Europe/London')

    def test_returns_dict(self):
        self.assertIsInstance(settings.accounts, DotDictionary)
