from django.views.decorators.http import require_safe, require_http_methods, require_POST
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe   # get 인 요청에만 실행 아니면 405 응답코드
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form' : form,
#     }
#     return render(request, 'articles/new.html', context)


@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid(): #form 은 유효성 검증
            article = form.save()   # 인스턴스 없으면 save 있으면 update
            return redirect('articles:detail', article.pk)
    else: # get  
        # new 
        form = ArticleForm()
    context = {     # 유효성 검사 통과못했을때
        'form' : form,
    }
    return render(request, 'articles/create.html', context)


    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance = article)
#     context = {
#         'article': article,
#         'form' : form,
#     }
#     return render(request, 'articles/edit.html', context)

@require_http_methods(['GET','POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance = article)
    context = {
        'article': article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)

    # article = Article.objects.get(pk=pk)
    # form = ArticleForm(request.POST, instance=article)
    # if form.is_valid():
    #     form.save()
    #     return redirect('articles:detail', article.pk)
    # context = {             # 실패한 폼 에러 메시지 
    #     'form' : form,
    # }
    # return render(request, 'articles/edit.html', context )
    
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    # return redirect('articles:detail', article.pk)