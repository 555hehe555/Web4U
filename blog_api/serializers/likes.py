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
        read_only_fields = ['id']  # user призначається через perform_create()


class DeleteUserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post']
        read_only_fields = ['id']

