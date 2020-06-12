from django.contrib.auth.models import User
from rest_framework import serializers

from apps.blog.models import Category, Blog, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogAndCommentsSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        return CommentSerializer(Comment.objects.filter(blog_id=obj.id), many=True).data

    class Meta:
        model = Blog
        fields = [
            'title',
            'slug',
            'body',
            'posted',
            'category',
            'enabled',
            'comments']
