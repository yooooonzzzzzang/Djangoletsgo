from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .serializers import ArticleSerializer
from .models import Article

# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article.html', context)


def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
                'id':article.pk,
                'title':article.title,
                'content':article.content,
                'created_at':article.created_at,
                'updated_at':article.updated_at,
            }
        )
    return JsonResponse(articles_json, safe=False)  # 딕셔너리가 아니면 safe=false 붙여줘야함

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type = 'application/json')



# 쿼리셋, 모델인스턴스 같은 복잡한 데이터를 json, xml 등 유형으로 쉽게 변환할 수 있는 python 데이터 타입으로 만들어줌
# @api_view(['GET'])
@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)    # -> json 나옴
