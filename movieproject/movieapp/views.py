from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from movieapp.models import Category,Movie
from reviewapp.models import Review


# Create your views here.
def demo(request):
    return render(request,'index.html')

def allMovieCat(request,c_slug=None):
    #user_id = request.GET.get('user_id')
    user_id = request.session.get('user_id')
    c_page=None
    movies_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        movies_list=Movie.objects.all().filter(category=c_page,available=True)
    else:
        movies_list=Movie.objects.all().filter(available=True)
    paginator=Paginator(movies_list,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        movies=paginator.page(page)
    except(EmptyPage,InvalidPage):
        movies=paginator.page(paginator.num_pages)
    return render(request,"home.html",{'category':c_page,'movies':movies})

def movDetail(request,c_slug,movie_slug):
    try:
        movie=Movie.objects.get(category__slug=c_slug,slug=movie_slug)
        movie_id = movie.id
        request.session['movie_id'] = movie_id
        user_id_in_session = request.session.get('user_id')
        # Check if the user_id of the selected movie matches the user_id in session
        has_permission = movie.user_id == user_id_in_session
        review_list = Review.objects.all().filter(movie=movie_id)
    except Exception as e:
        raise e
    return render(request, 'movie.html', {'movie': movie,'reviews':review_list, 'has_permission': has_permission})


def add(request):
    return render(request,'add.html')