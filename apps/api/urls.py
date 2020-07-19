"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from apps.api import views as api_views
from apps.api.views import movie_api, MoviesList
from rest_framework.authtoken import views as django_rest_views

urlpatterns = [
    path('movies/', MoviesList.as_view(), name='movies_list_api'),
    path('movies/<str:movie_imbd_id>/', movie_api.as_view(), name='api_spe_mov'),
    path('token/api-token-auth/',
         django_rest_views.obtain_auth_token, name='token_generating')
]
