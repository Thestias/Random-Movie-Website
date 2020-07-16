from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.randomovie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'imbd_id' ,'movie_title' ,'genero' ,'original_language' ,'overview' ,'poster_path' ,'release_date' ,'budget' ,'revenue' ,'runtime' ,'vote_average' ,'tagline']
