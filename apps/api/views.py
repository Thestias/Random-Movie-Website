from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.randomovie.models import Movie
from apps.api.serializers import MovieSerializer
from rest_framework import status

from rest_framework.views import APIView

class movie_api(APIView):
	'''
	This Views Handles the API for specific movies.

	URL = /api/id=MOVIE_IMBD_ID

	This View allows GET, POST, PUT and DELETE

	'''

	def get(self, request, movie_imbd_id):
		try:
			movie = Movie.objects.get(imbd_id=movie_imbd_id)
		except Movie.DoesNotExist:
			data = {}
			data['Error'] = 'Movie Not Found'
			return Response(data=data, status=status.HTTP_404_NOT_FOUND)
		else:
			serializer = MovieSerializer(movie)
			return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, movie_imbd_id):
		movie = Movie()
		serializer = MovieSerializer(movie, data=request.data)
		if serializer.is_valid():
			data = {}
			try:
				Movie.objects.get(imbd_id=request.data['imbd_id'])
			except Movie.DoesNotExist:
				serializer.save()
				data['Success'] = 'Operation Succesfull'
				return Response(data=data, status=status.HTTP_200_OK)
			else:
				data['Error'] = 'Already exists'
				return Response(data=data, status=status.HTTP_303_SEE_OTHER)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, movie_imbd_id): 
		data = {}
		try:
			movie = Movie.objects.get(imbd_id=movie_imbd_id)
		except Movie.DoesNotExist:
			data['Error'] = 'Record Not Found'
			return Response(data=data, status=status.HTTP_404_NOT_FOUND)
		else:
			serializer = MovieSerializer(movie, data=request.data, partial=True)   # Partial=True Allows for Partial Updates
			if serializer.is_valid():
				serializer.save()
				data['Success'] = 'Operation Succesfull'
				return Response(data=data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	def delete(self, request, movie_imbd_id):
		data = {}
		try:
			movie = Movie.objects.get(imbd_id=movie_imbd_id)
		except Movie.DoesNotExist:
			data['Error'] = 'Record Not Found'
			return Response(data=data, status=status.HTTP_404_NOT_FOUND)
		else:
			operation_delete = movie.delete()
			status_code = ''
			if operation_delete:
				data['Success'] = 'Operation Sucessfull'
				status_code = status.HTTP_200_OK
			else:
				data['Error'] = 'Operation Failed'
				status_code = status.HTTP_400_BAD_REQUEST
			return Response(data=data, status=status_code)
