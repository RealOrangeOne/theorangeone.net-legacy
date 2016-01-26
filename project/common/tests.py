from django.test import TestCase
from django.core.urlresolvers import reverse
import os.path
from django_dbq.models import Job
from . import jobs
from collections import namedtuple

PATH = os.path.dirname(os.path.abspath(__file__))


class CustomTemplateTestCase(TestCase):
    def setUp(self):
        self.template = 'pages:index'

    def test_accessable(self):
        response = self.client.get(reverse(self.template))
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        response = self.client.get(reverse(self.template))
        for item in ['html_title', 'body_class', 'js_redirect']:
            self.assertIn(item, response.context)


class ReverserTestCase(TestCase):
    REVERSER_IDENT = 'reverser:reverser'

    def test_reverser(self):
        response = self.client.post(reverse(self.REVERSER_IDENT), data={'ident': 'pages:index'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.data, reverse('pages:index'))

    def test_invalid_reverser(self):
        response = self.client.post(reverse(self.REVERSER_IDENT), data={'ident': 'pages:i-dont-exist'})
        self.assertEqual(response.status_code, 404)


class MarkdownViewTestCase(TestCase):
    def test_accessable(self):
        response = self.client.get(reverse('projects:project', args=['test']))
        self.assertEqual(response.status_code, 200)

    def test_parsing(self):
        response = self.client.get(reverse('projects:project', args=['test']))
        self.assertContains(response, '<h1>Testing</h1>')

    def test_template_engine(self):
        response = self.client.get(reverse('projects:project', args=['test']))
        self.assertContains(response, reverse('projects:all'))

    def test_invalid_template(self):
        response = self.client.get(reverse('projects:project', args=['not-a-project']))
        self.assertEqual(response.status_code, 404)


MockJob = namedtuple('MockJob', {'workspace': {}})


class WorkerTestCase(TestCase):
    def test_mail_job_creation(self):
        data = {
            'name': 'Person',
            'email': '123@123.123',
            'message': 'Hi there, things.'
        }
        workspace = {
            'template': 'email/contact_message.html',
            'from_email': data['email'],
            'to_email': 'info@theorangeone.net',
            'context': data
        }
        self.client.post(reverse('about:index'), data)
        self.assertEqual(Job.objects.count(), 1)
        job = Job.objects.all()[0]
        self.assertEqual(job.workspace, workspace)

    def test_email_error(self):
        data = {
            'name': 'Person',
            'email': '123@123.123',
            'message': 'Hi there, things.'
        }
        workspace = {
            'template': 'email/contact_message.html',
            'from_email': 'me@123.123',
            'to_email': data['email'],
            'context': data
        }
        job = MockJob(workspace)
        errors = None
        try:
            jobs.send_email(job)
        except Exception as e:
            errors = e

        self.assertFalse(errors)
