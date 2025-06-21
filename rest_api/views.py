from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema_view

from documentation.comments import comments_list_doc
from documentation.likes import like_list_doc
from documentation.posts import post_list_doc
from documentation.custom_user import user_list_doc
from .models import Post, Comments
from .permissions import IsOwner
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
    # GetUserLikeSerializer,
    GetAllUserLikeSerializer,
    CreateUserLikeSerializer,
    DeleteUserLikeSerializer,
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    DeleteCustomUserSerializer,
    PutCustomUserSerializer,
    PatchCustomUserSerializer
)


@extend_schema_view(
    list=post_list_doc,
    retrieve=post_list_doc,
    create=post_list_doc,
    destroy=post_list_doc,
    update=post_list_doc,
    partial_update=post_list_doc
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
    retrieve = comments_list_doc,
    create = comments_list_doc,
    destroy = comments_list_doc,
    update = comments_list_doc,
    partial_update = comments_list_doc
)
class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetCommentListSerializer
    queryset = Comments.objects.all()

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


@extend_schema_view(
    list=like_list_doc,
    retrieve=like_list_doc,
    create=like_list_doc,
    destroy=like_list_doc
)
class LikePostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    serializer_class = GetAllUserLikeSerializer
    queryset = Post.objects.all()

    def get_serializer_class(self):
        # if self.action == 'retrieve':
        #     return GetUserLikeSerializer
        if self.action == 'list':
            return GetAllUserLikeSerializer
        elif self.action == 'create':
            return CreateUserLikeSerializer
        elif self.action == 'destroy':
            return DeleteUserLikeSerializer
        return super().get_serializer_class()

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


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetCustomUserSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create']:
            return [permissions.AllowAny()]
        return [IsOwner()]

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCustomUserSerializer
        elif self.action == 'destroy':
            return DeleteCustomUserSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return GetCustomUserSerializer
        elif self.action == 'update':
            return PutCustomUserSerializer
        elif self.action == 'partial_update':
            return PatchCustomUserSerializer
        return super().get_serializer_class()