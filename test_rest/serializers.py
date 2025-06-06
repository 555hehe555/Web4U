from rest_framework import serializers
from .models import Post, Comments


class GetPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class CreatePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class DeletePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class PutPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']


class PatchPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date']





class GetCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'text_comments', 'post']


class CreateCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'text_comments', 'post']


class DeleteCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'text_comments', 'post']
