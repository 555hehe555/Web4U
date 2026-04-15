from rest_framework import serializers

from ..models import Like

class GetAllUserLikeSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Like
        fields = ['id', 'author', 'post']


class CreateUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id']
        read_only_fields = ['id']


class LikeListResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    results = GetAllUserLikeSerializer(many=True)
    user_liked = serializers.BooleanField()
    

class LikePaginatedResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.URLField(allow_null=True)
    previous = serializers.URLField(allow_null=True)
    results = GetAllUserLikeSerializer(many=True)
    user_liked = serializers.BooleanField()
