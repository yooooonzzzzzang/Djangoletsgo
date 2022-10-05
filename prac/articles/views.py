from django.shortcuts import render, redirect
from .models import article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = article.objects.all()
    context = {
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # articles = article(title=title, content=content)
    # articles.save()
    # return redirect('articles:index')
    # --------------model form 사용
    if request.method =='POST': # CREATE
        form = ArticleForm(request.POST)
        if form.is_valid():
            articles = form.save()
            return redirect('articles:detail', articles.pk)
    else:   # NEW
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/new.html', context )

def detail(request, pk):
    article1 = article.objects.get(pk=pk)
    context = {
        'article' : article1
    }
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article1 = article.objects.get(pk=pk)
    form = ArticleForm(instance=article1)
    context = {
        'article':article1,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article1 = article.objects.get(pk=pk)
    # article1.title = request.POST.get('title')
    # article1.cont
    # ent = request.POST.get('content')
    # article1.save()
    # return redirect('articles:detail', article1.pk)
    if request.method == 'POST':    # update
        form = ArticleForm(request.POST, instance=article1)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article1.pk)
    else:   # edit
            form = ArticleForm(instance=article1)
    context = {
        'form' : form,
        'article':article1,
    }
    return render(request, 'articles/edit.html', context)
def delete(request, pk):
    article1 = article.objects.get(pk=pk)
    if request.method =='POST':
        article1.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article1.pk)