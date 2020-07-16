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
from apps.api.views import movie_api
urlpatterns = [
    path('id=<str:movie_imbd_id>/',
         movie_api.as_view(), name='api_spe_mov'),
    # path('create', api_views.api_create_movie, name='api_create_movie'),
    # path('delete/id=<str:imbd_id_req>', api_views.api_delete_movie, name='api_delete_movie'),
    # path('update/id=<str:imbd_id_req>', api_views.api_update_movie, name='api_update_movie')
]
