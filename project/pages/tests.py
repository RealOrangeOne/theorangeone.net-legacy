from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
import os.path, json


class AboutTestCase(TestCase):
    def test_website_accessable(self):
        response = self.client.get(reverse('about:website'))
        self.assertEqual(response.status_code, 200)

    def test_me_accessable(self):
        response = self.client.get(reverse('about:me'))
        self.assertEqual(response.status_code, 200)

    def test_index_accessable(self):
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


class CorePagesTestCase(TestCase):
    def test_404_accessable(self):
        response = self.client.get(reverse('404'))
        self.assertEqual(response.status_code, 404)

    def test_no_js_accessable(self):
        response = self.client.get(reverse('no-js'))
        self.assertEqual(response.status_code, 200)

    def test_index_accessable(self):
        response = self.client.get(reverse('pages:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_projects(self):
        projects = json.load(open(os.path.join(settings.BASE_DIR, 'data/projects.json')))
        response = self.client.get(reverse('pages:index'))
        for key, project in projects.items():
            self.assertContains(response, project['title'])
            if 'image' in project:
                self.assertContains(response, project['image'])


class ProjectsTestCase(TestCase):
    def test_all_accessable(self):
        response = self.client.get(reverse('projects:all'))
        self.assertEqual(response.status_code, 200)

    def test_test_project_accessable(self):
        response = self.client.get(reverse('projects:project', args=['test']))
        self.assertEqual(response.status_code, 200)

    def test_projects_accessable(self):
        projects = json.load(open(os.path.join(settings.BASE_DIR, 'data/projects.json')))
        for key, project in projects.items():
            response = self.client.get(reverse('projects:project', args=[key]))
            self.assertEqual(response.status_code, 200)

    def test_projects_details(self):
        projects = json.load(open(os.path.join(settings.BASE_DIR, 'data/projects.json')))
        for key, project in projects.items():
            response = self.client.get(reverse('projects:project', args=[key]))
            self.assertContains(response, project['title'])
            if 'image' in project:
                self.assertContains(response, project['image'])


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

    def test_2015_code_accessable(self):
        response = self.client.get(reverse('robotics:2015-code'))
        self.assertEqual(response.status_code, 200)


class CollegeTestCase(TestCase):
    def test_attack_on_blocks_accessable(self):
        response = self.client.get(reverse('college:attack-on-blocks'))
        self.assertEqual(response.status_code, 200)

    def test_student_server_accessable(self):
        response = self.client.get(reverse('college:student-server'))
        self.assertEqual(response.status_code, 200)
