from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema_view

from documentation import (
    comments_list_doc,
    comments_create_doc,
    comments_update_doc,
    comments_patch_doc,
    comments_delete_doc,
)

from ..models import Comments, Post
from ..permissions import IsOwnerOrReadOnly
from ..serializers import (
    GetCommentListSerializer,
    CreateCommentListSerializer,
    DeleteCommentListSerializer,
    PutCommentListSerializer,
    PatchCommentListSerializer
)

@extend_schema_view(
    list=comments_list_doc,
    retrieve=comments_list_doc,
    create=comments_create_doc,
    destroy=comments_delete_doc,
    update=comments_update_doc,
    partial_update=comments_patch_doc
)
class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = GetCommentListSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'comment_pk'

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get("post_pk"))

    def get_queryset(self):
        post = self.get_post()
        return Comments.objects.filter(post=post).order_by('-date')

    def get_serializer_class(self):
        if self.action == 'list':
            return GetCommentListSerializer
        elif self.action == 'create':
            return CreateCommentListSerializer
        elif self.action == 'destroy':
            return DeleteCommentListSerializer
        elif self.action == 'update':
            return PutCommentListSerializer
        elif self.action == 'partial_update':
            return PatchCommentListSerializer
        elif self.action == 'retrieve':
            return GetCommentListSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(user=self.request.user, post=post)
