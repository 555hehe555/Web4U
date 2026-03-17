from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from drf_spectacular.utils import extend_schema_view

from documentation import comments_list_doc

from ..models import Comments
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
    create=comments_list_doc,
    destroy=comments_list_doc,
    update=comments_list_doc,
    partial_update=comments_list_doc
)
class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = GetCommentListSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get("post_pk")  # беремо id поста з url
        return Comments.objects.filter(post_id=post_pk).order_by('-date')

    def get_serializer_class(self):
        if self.action == 'list':
            return GetCommentListSerializer
        if self.action == 'create':
            return CreateCommentListSerializer
        elif self.action == 'destroy':
            return DeleteCommentListSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return GetCommentListSerializer
        elif self.action == 'update':
            return PutCommentListSerializer
        elif self.action == 'partial_update':
            return PatchCommentListSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")  # щоб коментар завжди був до цього поста
        serializer.save(user=self.request.user, post_id=post_pk)
