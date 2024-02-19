from django.http import HttpResponse
from django.shortcuts import render, redirect
from movieapp.models import Movie,Category
from .models import Review

# Create your views here.
def rate(request):
    user_id = request.session.get('user_id')
    movie_id = request.session.get('movie_id')
    if request.method == "POST":
        rating=request.POST.get('rating')
        comments= request.POST.get('comments')
        rate_star=Review(rating=rating,comments=comments,user_id=user_id,movie_id=movie_id)
        rate_star.save()
        return redirect('movieapp:allMovieCat')
    return render(request,'review.html')
