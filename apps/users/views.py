from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from apps.randomovie.models import UserFavoriteMovies, Movie
from apps.randomovie.views import movie_details
# Create your views here.


def register(request):
    if request.method == 'POST':
        # Le envia los datos del POST al FORM para guardar i asume
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('login')

    else:
        register_form = RegisterForm()  # Crea un form vacio

    return render(request, 'users/register.html', context={'register_form': register_form})


@login_required
def profile(request):
    if request.method == 'GET':
        lista_movies = []
        user_saved_movies = UserFavoriteMovies.objects.filter(
            user=request.user).values_list('favorited_movie_id')  # Searches for all movies favorited by user
        for imbd_id_req in user_saved_movies:
            lista_movies.append(movie_details(
                Movie.objects.get(imbd_id=imbd_id_req[0])))
        return render(request, 'users/profile.html', context={'lista_movies': lista_movies})
