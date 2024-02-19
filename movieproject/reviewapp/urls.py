from django.urls import path

from reviewapp import views


app_name = 'reviewapp'

urlpatterns = [

    path('rate/', views.rate, name='rate'),
    ]
