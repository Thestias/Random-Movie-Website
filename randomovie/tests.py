from django.test import TestCase
from django.urls import resolve
from randomovie.views import homepage

# Create your tests here.

class HomePageTest(TestCase):

    def test_url_resolves_to_homepage_view(self):
        find = resolve('/')
        self.assertEqual(find.func, homepage)
