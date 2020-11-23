from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Movie(models.Model):
    movie_id = models.IntegerField()
    imbd_id = models.CharField(max_length=200)
    movie_title = models.CharField(max_length=500)
    genero = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    overview = models.CharField(max_length=50000)
    poster_path = models.CharField(max_length=5000)
    release_date = models.CharField(max_length=200)
    budget = models.CharField(max_length=200)
    revenue = models.CharField(max_length=200)
    runtime = models.CharField(max_length=200)
    vote_average = models.CharField(max_length=200)
    tagline = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.movie_id} {self.imbd_id} {self.movie_title}'


class UserFavoriteMovies(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    favorited_movie_id = models.CharField(max_length=200)
