from django.shortcuts import render, get_object_or_404
from apps.randomovie.models import Movie, UserFavoriteMovies
from utils.movie_details_from_db import movie_details
import random
from django.contrib import messages

# Create your views here.


def favorited_movies(request):
    lista__favorited_movies = []
    imbd_ides = []
    user_saved_movies = UserFavoriteMovies.objects.filter(
        user=request.user).values_list('favorited_movie_id')
    for imbd_id_req in user_saved_movies:
        if imbd_id_req[0] == 'imdb id Not Found':
            pass
        else:
            lista__favorited_movies.append(movie_details(
                Movie.objects.get(imbd_id=imbd_id_req[0])))
    for i in lista__favorited_movies:
        imbd_ides.append(i.get('imbd_id'))

    return imbd_ides


def homepage(request):
    ammount_items = Movie.objects.count()
    rand_movie_id = random.randint(1, ammount_items)
    movie_det_homepage = get_object_or_404(Movie, id=rand_movie_id)
    homepage_context = movie_details(movie_det_homepage)
    if request.user.is_authenticated:
        if request.method == 'POST':
            imbd_id_obtaining = dict(request.POST)
            imbd_id_obtaining = imbd_id_obtaining['imbd_id'][0]
            form = UserFavoriteMovies(
                favorited_movie_id=imbd_id_obtaining, user=request.user)
            form.save()
            messages.success(request, f'Movie added to your favorites!')
        lista_movies_favoritas = favorited_movies(request)
        homepage_context['favorited_movies'] = lista_movies_favoritas

    return render(request, 'homepage/index.html', context=homepage_context)


def about(request):
    return render(request, 'about/about.html')


def specific_movie(request, imbd_id_req):
    movie_det_specific = Movie.objects.get(imbd_id=imbd_id_req)
    det_movie = movie_details(movie_det_specific)
    if request.user.is_authenticated:
        lista_movies_favoritas = favorited_movies(request)
        det_movie['favorited_movies'] = lista_movies_favoritas
        if request.method == 'POST':
            imbd_id_obtaining = dict(request.POST)
            imbd_id_obtaining = imbd_id_obtaining['imbd_id'][0]
            if 'no' in imbd_id_obtaining:
                delete_favorito = UserFavoriteMovies.objects.get(
                    favorited_movie_id=imbd_id_obtaining[3:])
                delete_favorito.delete()
                messages.error(request, 'Movie Deleted From Favorites.')
            else:
                form = UserFavoriteMovies(
                    favorited_movie_id=imbd_id_obtaining, user=request.user)
                form.save()
                messages.success(request, f'Movie added to your favorites!')
    return render(request, 'homepage/index.html', context=det_movie)
