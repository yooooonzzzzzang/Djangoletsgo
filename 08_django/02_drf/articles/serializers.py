from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__' 
        # 기존에 있는 필드
        read_only_fields = ('article',)


class ArticleSerializer(serializers.ModelSerializer):
    # comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)          # 추가되거나 오버라이드되는 애들
    comment_count = serializers.IntegerField(source='comment_set.count',read_only=True)
    class Meta:
        model = Article
        fields = '__all__'



