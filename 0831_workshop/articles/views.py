from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
# 데이터베이스에 저장된 데이터를 가져와서 조회하려면 데이터 context에 넣고 뿌려야함
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request,'articles/new.html')

# 요청 데이터베이스에 데이터 저장하기 
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:index')
