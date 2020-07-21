from django.test import TestCase
from django.urls import resolve, reverse
from apps.randomovie.views import homepage, about, specific_movie
from utils.create_model_objects_for_test import obj_movie_mod_create
from apps.randomovie.models import Movie
# Create your tests here.


class ViewMatchTest(TestCase):

    def setUp(self):
        obj_movie_mod_create()

    def test_homepage_view(self):
        # The resolve() function finds the view that matches the given url
        find = resolve('/')
        self.assertEqual(find.func, homepage)

    def test_about_view(self):
        find = resolve('/about/')
        self.assertEqual(find.func, about)

    def test_specific_movie_view(self):
        find = resolve('/id=tt0478970/')
        self.assertEqual(find.func, specific_movie)


class PageStatusOkTest(TestCase):
    '''
        This Class Tests that all views return the status code 200.
    '''

    def setUp(self):
        obj_movie_mod_create()

    def test_homepage_status_code_to_ok(self):
        url = reverse('homepage')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_status_code_to_ok(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_specify_movie_status_code_to_ok(self):
        url = reverse('specify_movie', args=['tt3783958'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class MovieModelTest(TestCase):
    ''' 
        This class tests the str method in the model Movie
    '''

    def setUp(self):
        obj_movie_mod_create()

    def test_model_str(self):
        movie_one = Movie.objects.get(id=1)
        self.assertEqual(str(movie_one), '1 tt0478970 Ant-Man')
