from django.contrib import admin
from .models import Movie
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ('movie_id', 'imbd_id', 'movie_title', 'genero', 'original_language', 'release_date', 'runtime', 'vote_average', 'tagline',)
	list_per_page = 15
	list_filter = ('genero',)
