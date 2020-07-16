from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.randomovie.models import Movie
from apps.api.serializers import MovieSerializer
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def api_get_movie(request, movie_id):
	'''
	This view get's data from a movie specified in the url, with the IMBD ID
	'''
	data = {}
	try:
		movie = Movie.objects.get(imbd_id=movie_id)
	except Movie.DoesNotExist:
		data['failure'] = 'record not found'
		return Response(data=data, status=status.HTTP_404_NOT_FOUND)
	else:
		serializer = MovieSerializer(movie)
		return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def api_create_movie(request):
	'''
	This view creates a movie
	'''
	movie = Movie()
	serializer = MovieSerializer(movie, data=request.data)
	if serializer.is_valid():
		data = {}
		try:
			Movie.objects.get(imbd_id=request.data['imbd_id'])
		except Movie.DoesNotExist:
			serializer.save()
			data['success'] = 'operation succesfull'
			return Response(data=data, status=status.HTTP_200_OK)
		else:
			data['exist'] = 'record already exists'
			return Response(data=data, status=status.HTTP_303_SEE_OTHER)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def api_update_movie(request, imbd_id_req):
	data = {}
	try:
		movie = Movie.objects.get(imbd_id=imbd_id_req)
	except Movie.DoesNotExist:
		data['failure'] = 'record not found'
		return Response(data=data, status=status.HTTP_404_NOT_FOUND)
	else:
		serializer = MovieSerializer(movie, data=request.data, partial=True)  # Partial Allows for Partial Updates
		if serializer.is_valid():
			serializer.save()
			data['success'] = 'operation succesfull'
			return Response(data=data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def api_delete_movie(request, imbd_id_req):
	'''
	This view DELETES a Movie Specified in the URL using the IMBD ID
	'''
	data = {}
	try:
		movie = Movie.objects.get(imbd_id=imbd_id_req)
	except Movie.DoesNotExist:
		data['failure'] = 'record not found'
		return Response(data=data, status=status.HTTP_404_NOT_FOUND)
	else:
		operation_delete = movie.delete()
		if operation_delete:
			data['success'] = 'operation succesfull'
		else:
			data['failure'] = 'operation failed'
		return Response(data=data)
