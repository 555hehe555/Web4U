from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema_view

from documentation.comments import comments_list_doc
from .models import Post, Comments
from .serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
    DeletePostsListSerializer,
    PutPostsListSerializer,
    PatchPostsListSerializer,
    GetCommentListSerializer,
    CreateCommentListSerializer,
    DeleteCommentListSerializer,
    PutCommentListSerializer,
    PatchCommentListSerializer,
    GetUserLikeSerializer,
    GetAllUserLikeSerializer,
    CreateUserLikeSerializer,
    DeleteUserLikeSerializer
)


class PostModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetPostsListSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreatePostsListSerializer
        elif self.action == 'destroy':
            return DeletePostsListSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return GetPostsListSerializer
        elif self.action == 'update':
            return PutPostsListSerializer
        elif self.action == 'partial_update':
            return PatchPostsListSerializer
        return super().get_serializer_class()


@extend_schema_view(
    list = comments_list_doc,
    retrieve = comments_list_doc
)
class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetCommentListSerializer
    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return GetCommentListSerializer
        if self.action == 'create':
            return CreatePostsListSerializer
        elif self.action == 'destroy':
            return DeletePostsListSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return GetPostsListSerializer
        elif self.action == 'update':
            return PutPostsListSerializer
        elif self.action == 'partial_update':
            return PatchPostsListSerializer
        return super().get_serializer_class()


class LikePostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    serializer_class = GetUserLikeSerializer
    queryset = Post.objects.all()

    # @swagger_auto_schema(manual_parameters=[post_pk_param])
    # def list(self, request, post_pk=None):
    #     return super().list(request)
    #
    # @swagger_auto_schema(manual_parameters=[post_pk_param])
    # def create(self, request, post_pk=None):
    #     return super().create(request)
    #
    # @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    # def retrieve(self, request, post_pk=None, pk=None):
    #     return super().retrieve(request, pk)
    #
    # @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    # def destroy(self, request, post_pk=None, pk=None):
    #     return super().destroy(request, pk)
