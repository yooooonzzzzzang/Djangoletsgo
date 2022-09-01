from django.shortcuts import render, redirect

import articles
from .models import Articles
# Create your views here.
def index(request):
    articles = Articles.objects.order_by('-id')
    context = {
        'articles':articles,
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Articles(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Articles.objects.get(pk=pk)    #키= value
    context = {
        'article' : article,
    } 
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Articles.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    article = Articles.objects.get(pk=pk)   
    context ={
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Articles.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save() 
    return redirect('articles:detail', article.pk)