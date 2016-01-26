from django.test import TestCase
from django.core.urlresolvers import reverse


class IndexTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)


class AboutWebsiteTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('about:website'))
        self.assertEqual(response.status_code, 200)


class AboutIndexTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)

    def test_email_send(self):
        data = {
            'email': '123@123.123',
            'name': 'Person',
            'message': 'Hi there, things.'
        }
        response = self.client.post(reverse('about:index'), data)
        self.assertRedirects(response, '/about/?sent')

    def test_success_message_shows(self):
        response = self.client.get(reverse('about:index') + '?sent')
        self.assertContains(response, 'Already Sent')


class Custom404TestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 404)


class NoJavascriptTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('no-js'))
        self.assertEqual(response.status_code, 200)


class AllProjectsTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('projects:all'))
        self.assertEqual(response.status_code, 200)


class RoboticsTestCase(TestCase):
    def test_2015_index_accessable(self):
        response = self.client.get(reverse('robotics:2015-index'))
        self.assertEqual(response.status_code, 200)

    def test_2014_index_accessable(self):
        response = self.client.get(reverse('robotics:2014-index'))
        self.assertEqual(response.status_code, 200)

    def test_2015_robot_accessable(self):
        response = self.client.get(reverse('robotics:2015-robot'))
        self.assertEqual(response.status_code, 200)
