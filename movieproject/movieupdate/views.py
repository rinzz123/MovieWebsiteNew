from django.shortcuts import render, redirect, get_object_or_404
from movieapp.models import Movie,Category
from .forms import MovieForm
app_name='movieupdate'
# Create your views here.
def add_movie(request):
    user_id = request.session.get('user_id')
    if request.method == "POST":
        name=request.POST.get('name')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        actors = request.POST.get('actors')
        category = request.POST.get('category')
        poster = request.FILES['poster']
        link = request.POST.get('link')
        movie=Movie(name=name,slug=name,description=description,release_date=release_date,actors=actors,poster=poster,link=link,category_id=category,user_id=user_id)
        movie.save()
        return redirect('movieapp:allMovieCat')
    return render(request,'add.html')

def edit(request,id):
    movie=get_object_or_404(Movie,id=id)
    if request.method == 'POST':
        form=MovieForm(request.POST or None,request.FILES,instance=movie)
        if form.is_valid():
         form.save()
        return redirect('movieapp:allMovieCat')
    else:
        form = MovieForm(instance=movie)
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('movieapp:allMovieCat')
    return render(request,'delete.html')