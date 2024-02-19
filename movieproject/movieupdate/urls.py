from django.urls import path

from movieupdate import views


app_name = 'movieupdate'

urlpatterns = [

    path('add/', views.add_movie, name='add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    ]
