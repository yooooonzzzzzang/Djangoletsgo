from django.shortcuts import render, redirect
from .models import Article

# Create your views here.


def read(request):
    articles = Article.objects.order_by('id')
    context = {'articles': articles}
    return render(request, 'articles/read.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
