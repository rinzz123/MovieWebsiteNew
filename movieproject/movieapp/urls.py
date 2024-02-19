from django.contrib import admin
from django.urls import path, include

from movieapp import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.demo, name='demo'),
    path('movie/', views.allMovieCat, name='allMovieCat'),
    path('<slug:c_slug>/', views.allMovieCat, name='movies_by_category'),
    path('<slug:c_slug>/<slug:movie_slug>/', views.movDetail, name='movCatdetail'),



]
