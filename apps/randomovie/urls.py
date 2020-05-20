"""random_movie_project URL Configuration

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
from apps.randomovie import views as random_movie_views

urlpatterns = [
    path('', random_movie_views.homepage, name='homepage'),
    path('about/', random_movie_views.about, name='about'),
    # Always at the end.
    path('id=<str:imbd_id_req>/',
         random_movie_views.specific_movie, name='specify_movie'),
]
