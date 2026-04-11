from rest_framework import serializers

from ..models import Comments

class GetCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class CreateCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'user', 'post', 'date']
        read_only_fields = ['id', 'user', 'post', 'date']

class DeleteCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class PutCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'user', 'post', 'date']
        read_only_fields = ['id', 'post', 'user', 'date']


class PatchCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'user', 'post', 'date']
        read_only_fields = ['id', 'post', 'user', 'date']

