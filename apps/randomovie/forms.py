from django import forms
from .models import UserFavoriteMovies
from django.forms import ModelForm


class FavoritedMovieForm(ModelForm):
    favorited_movie_id = forms.CharField(max_length=200)

    class Meta:
        model = UserFavoriteMovies
        fields = ['favorited_movie_id']
