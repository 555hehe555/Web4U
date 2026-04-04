from rest_framework import serializers

from ..models import Comments

class GetCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class CreateCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'post']
        read_only_fields = ['id']  # user додається через perform_create()


class DeleteCommentListSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'date', 'user', 'post']


class PutCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments', 'post']
        read_only_fields = ['id']


class PatchCommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text_comments']
        read_only_fields = ['id']

