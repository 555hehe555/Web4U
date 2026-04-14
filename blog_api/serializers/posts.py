from rest_framework import serializers

from ..models import Post


class GetPostsListSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "description", "img", "author", "date"]


class CreatePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "description", "img"]


class UpdatePostsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "description", "img"]
        