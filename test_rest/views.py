from django.contrib.auth.models import User
from drf_yasg.inspectors import SwaggerAutoSchema

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets, permissions, generics

from .permissions import IsOwnerOrReadOnly
from blog.models import CustomUser

from .models import Post, Comments
from .serializers import GetPostsListSerializer, CreatePostsListSerializer, DeletePostsListSerializer, \
    PutPostsListSerializer, PatchPostsListSerializer
from .serializers import GetCommentListSerializer, CreateCommentListSerializer, DeleteCommentListSerializer\
    , PutCommentListSerializer, PatchCommentListSerializer
from .serializers import (GetUserLikeSerializer, GetAllUserLikeSerializer, \
                          CreateUserLikeSerializer, DeleteUserLikeSerializer)

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

post_pk_param = openapi.Parameter(
    'post_pk',
    openapi.IN_PATH,
    description="ID поста",
    type=openapi.TYPE_INTEGER
)

pk_param = openapi.Parameter(
    'id',
    openapi.IN_PATH,
    description="ID",
    type=openapi.TYPE_INTEGER
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


class CommentsAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        return ['Comments']


class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetCommentListSerializer
    queryset = Comments.objects.all()

    @swagger_auto_schema(manual_parameters=[post_pk_param])
    def list(self, request, post_pk=None):
        return super().list(request)

    @swagger_auto_schema(manual_parameters=[post_pk_param])
    def create(self, request, post_pk=None):
        return super().create(request)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def retrieve(self, request, post_pk=None, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def destroy(self, request, post_pk=None, pk=None):
        return super().destroy(request, pk)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def update(self, request, post_pk=None, pk=None):
        return super().update(request, pk)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def partial_update(self, request, post_pk=None, pk=None):
        return super().partial_update(request, pk)

    swagger_schema = CommentsAutoSchema


class LikeAutoSchema(SwaggerAutoSchema):
    def get_tags(self, operation_keys=None):
        return ['Like']


class LikePostViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete']
    serializer_class = GetUserLikeSerializer
    queryset = Post.objects.all()

    @swagger_auto_schema(manual_parameters=[post_pk_param])
    def list(self, request, post_pk=None):
        return super().list(request)

    @swagger_auto_schema(manual_parameters=[post_pk_param])
    def create(self, request, post_pk=None):
        return super().create(request)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def retrieve(self, request, post_pk=None, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(manual_parameters=[post_pk_param, pk_param])
    def destroy(self, request, post_pk=None, pk=None):
        return super().destroy(request, pk)

    swagger_schema = LikeAutoSchema


