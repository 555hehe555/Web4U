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


class PutCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'text_comments', 'post']


class PatchCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'name', 'text_comments', 'post']



class GetUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['liked_by']


class GetAllUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['liked_by']


class CreateUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['liked_by']


class DeleteUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['liked_by']