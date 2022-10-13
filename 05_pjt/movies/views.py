from multiprocessing import context
from django.urls import is_valid_path
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.shortcuts import redirect, render
from .models import Movie
from .forms import MovieForm
# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.all()
    
    context = {
        'movies':movies,
       
    }
    return render(request, 'movies/index.html', context)


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method =='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies:index')

    else:
        form =  MovieForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/create.html',context) 


@require_safe
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html',context)

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/update.html', context)


def delete(request, pk):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
    return redirect('movies:index')