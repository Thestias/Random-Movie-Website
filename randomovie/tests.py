from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from randomovie.views import homepage
from randomovie.models import Movie

# Create your tests here.


class HomePageTest(TestCase):
    Movie.objects.create(id=900)

    def test_url_resolves_to_homepage_view(self):
        find = resolve('/')
        self.assertEqual(find.func, homepage)

    def test_url_status_code_to_ok(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
