from rest_framework import serializers

from ..models import Post

class GetPostsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'img', 'author', 'date']


class CreatePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'description', 'img']
        read_only_fields = ['id']  # author не передається, додається в perform_create()


class DeletePostsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'img', 'author', 'date']


class PutPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'img']
        read_only_fields = ['id']


class PatchPostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'img']
        read_only_fields = ['id']