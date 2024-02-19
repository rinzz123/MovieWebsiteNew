from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('movieapp:movies_by_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Movie(models.Model):
    objects = None
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    poster = models.ImageField(upload_to='movies')
    description = models.TextField(blank=True)
    release_date = models.DateTimeField(auto_now_add=True)
    actors = models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    link = models.URLField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    available=models.BooleanField(default=True)

    def get_url(self):
        return reverse('movieapp:movCatdetail', args=[self.category.slug, self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def __str__(self):
        return '{}'.format(self.name)
