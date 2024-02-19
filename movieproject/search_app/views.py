from django.shortcuts import render
from movieapp.models import Movie
from django.db.models import Q
# Create your views here.
def SearchResult(request):
    movies=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        movies = Movie.objects.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
    return render(request,'search.html',{'query':query,'movies':movies})
