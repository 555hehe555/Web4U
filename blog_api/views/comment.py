from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema_view

from documentation import (
    comments_list_doc,
    comments_retrieve_doc,
    comments_create_doc,
    comments_update_doc,
    comments_patch_doc,
    comments_delete_doc,
)

from ..models import Comments, Post
from ..permissions import IsOwnerOrReadOnly
from ..serializers import (
    CommentReadSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
)


@extend_schema_view(
    list=comments_list_doc,
    retrieve=comments_retrieve_doc,
    create=comments_create_doc,
    update=comments_update_doc,
    partial_update=comments_patch_doc,
    destroy=comments_delete_doc,
)
class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = CommentReadSerializer
    lookup_field = "pk"
    lookup_url_kwarg = "comment_pk"

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_pk"))

    def get_queryset(self):
        post = self.get_post()
        return (
            Comments.objects
            .filter(post=post)
            .select_related("user")
            .order_by("-date", "-id")
        )

    def get_serializer_class(self):
        if self.action == "create":
            return CommentCreateSerializer
        if self.action in ["update", "partial_update"]:
            return CommentUpdateSerializer
        return CommentReadSerializer

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(user=self.request.user, post=post)
