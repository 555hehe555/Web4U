from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_spectacular.utils import extend_schema_view

from documentation import post_list_doc

from ..models import Post
from ..permissions import IsOwnerOrReadOnly
from ..serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
    DeletePostsListSerializer,
    PutPostsListSerializer,
    PatchPostsListSerializer
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
    template_settings_list = 'blog.html'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetPostsListSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Post.objects.all().order_by('-date')

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

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
