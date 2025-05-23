from django.contrib.auth.models import User

from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers, viewsets, permissions, generics

from .permissions import IsOwnerOrReadOnly
from blog.models import CustomUser

from .models import Post
from .serializers import GetPostsListSerializer, CreatePostsListSerializer, DeletePostsListSerializer, \
    PutPostsListSerializer, PatchPostsListSerializer


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
