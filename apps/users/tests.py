from django.test import TestCase
from apps.users.views import register
from django.contrib.auth import views as auth_views
from django.urls import resolve, reverse
# Create your tests here.


class PageStatusOkTest(TestCase):
    '''
        This Class Tests that all views return the status code 200.
    '''

    def test_login_status_code_to_ok(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_status_code_to_ok(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
