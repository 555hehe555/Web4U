from django.contrib.auth.models import User

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets, permissions, generics

from .permissions import IsOwnerOrReadOnly
from blog.models import CustomUser

from .models import Post, Comments
from .serializers import GetPostsListSerializer, CreatePostsListSerializer, DeletePostsListSerializer, \
    PutPostsListSerializer, PatchPostsListSerializer
from .serializers import GetCommentListSerializer, CreateCommentListSerializer, DeleteCommentListSerializer


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


class CommentModelViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    serializer_class = GetCommentListSerializer
    queryset = Comments.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCommentListSerializer
        elif self.action == 'destroy':
            return DeleteCommentListSerializer
        elif self.action == 'retrieve' or self.action == 'list':
            return GetCommentListSerializer
        return super().get_serializer_class()