from django.db import models
from movieapp.models import Movie
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    objects = None
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    comments=models.TextField()
    rating=models.IntegerField()



