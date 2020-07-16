from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.randomovie.models import Movie
from apps.api.serializers import MovieSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def movie_api_view(request, movie_id):
	try:
		movie = Movie.objects.get(imbd_id=movie_id)
	except Movie.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
	else:
		serializer = MovieSerializer(movie)
		return Response(serializer.data)