from django.test import TestCase
from django.core.urlresolvers import reverse
import os.path
from django_dbq.models import Job
from . import jobs
from collections import namedtuple

PATH = os.path.dirname(os.path.abspath(__file__))

MockJob = namedtuple('MockJob', {'workspace': {}}) 

class WorkerTestCase(TestCase):
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
