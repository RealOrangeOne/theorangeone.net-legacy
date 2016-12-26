from project.common.tests import BaseTestCase
from .models import ProjectPage, validate_url, ALLOWED_DOMAINS
from django.core.exceptions import ValidationError


class ProjectPageTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.create_model(ProjectPage, {
            'title': 'Test',
            'body': 'test',
            'download_url': 'https://github.com/test',
            'project_url': 'https://github.com/test'
        })
        self.project = ProjectPage.objects.first()

    def test_page(self):
        response = self.client.get(self.project.url)
        self.assertEqual(response.status_code, 200)
        content = self.parse_content(response.content)
        self.assertIn(self.project.title, content.title.string)

    def test_download_url(self):
        self.assertEqual(self.project.get_download_url(), self.project.download_url)

    def test_validator_on_model(self):
        response = self.create_model(ProjectPage, {
            'title': 'Test',
            'body': 'test',
            'download_url': 'https://github.com/test',
            'project_url': 'https://foo.com/test'
        })
        self.assertNotEqual(response.status_code, 302)
        response = self.create_model(ProjectPage, {
            'title': 'Test',
            'body': 'test',
            'download_url': 'https://foo.com/test',
            'project_url': 'https://github.com/test'
        })
        self.assertNotEqual(response.status_code, 302)

    def test_validator(self):
        for domain in ALLOWED_DOMAINS:
            validate_url('https://{}.com/test'.format(domain))

        with self.assertRaises(ValidationError):
            validate_url('https://foo.com')
