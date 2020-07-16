from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.randomovie.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_title', 'genero']
