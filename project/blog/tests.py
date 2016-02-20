from django.test import TestCase
import requests_mock, json
from . import utils
from django.core.urlresolvers import reverse


@requests_mock.mock()
class WordPressTestCase(TestCase):
    def setUp(self):
        self.test_blog_data = {
            "title": "Test Blog Post",
            "ID": 1,
            "content": "<p>Test blog post content</p>",
            "slug": "test-post"
        }
        self.invalid_blog_data = {
            "title": "Invalid blog post",
            "content": "<p></p>",
            "slug": "invalid"
        }

    def test_gets_correct_data(self, m):
        payload = json.dumps(self.test_blog_data)
        m.get(utils.build_url(self.test_blog_data['slug']), text=payload)
        blog_data = utils.get_post(self.test_blog_data['slug'])
        self.assertEqual(blog_data, self.test_blog_data)

    def test_invalid_response(self, m):
        payload = json.dumps(self.invalid_blog_data)
        m.get(utils.build_url(self.invalid_blog_data['slug']), text=payload)
        blog_data = utils.get_post(self.invalid_blog_data['slug'])
        self.assertFalse(blog_data)

    def test_invalid_status(self, m):
        payload = json.dumps(self.test_blog_data)
        m.get(utils.build_url(self.test_blog_data['slug']), text=payload, status_code=500)
        blog_data = utils.get_post(self.test_blog_data['slug'])
        self.assertFalse(blog_data)

    def test_no_slug(self, m):
        blog_data = utils.get_post('')
        self.assertFalse(blog_data)


@requests_mock.mock()
class BlogViewTestCase(TestCase):
    def setUp(self):
        self.test_blog_data = {
            "title": "Test Blog Post",
            "ID": 1,
            "content": "<p>Test blog post content</p>",
            "slug": "test-post",
            "date": "2000-01-01T18:05:00+00:00"
        }

    def test_accessable(self, m):
        payload = json.dumps(self.test_blog_data)
        m.get(utils.build_url(self.test_blog_data['slug']), text=payload)
        response = self.client.get(reverse('blog:blog-post', args=[self.test_blog_data['slug']]))
        self.assertEqual(response.status_code, 200)

    def test_correct_content(self, m):
        payload = json.dumps(self.test_blog_data)
        m.get(utils.build_url(self.test_blog_data['slug']), text=payload)
        response = self.client.get(reverse('blog:blog-post', args=[self.test_blog_data['slug']]))
        self.assertContains(response, self.test_blog_data['content'])
        self.assertEqual(response.context['html_title'], self.test_blog_data['title'])
