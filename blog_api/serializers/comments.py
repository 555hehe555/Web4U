from rest_framework import serializers

from ..models import Comments


class CommentReadSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "text_comments", "date", "user", "post"]


class CommentCreateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "text_comments", "user", "post", "date"]
        read_only_fields = ["id", "user", "post", "date"]


class CommentUpdateSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Comments
        fields = ["id", "text_comments", "user", "post", "date"]
        read_only_fields = ["id", "user", "post", "date"]
