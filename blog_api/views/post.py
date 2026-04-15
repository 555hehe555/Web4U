from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from drf_spectacular.utils import extend_schema_view

from documentation import (
    post_list_doc,
    post_retrieve_doc,
    post_create_doc,
    post_update_doc,
    post_patch_doc,
    post_delete_doc,
)

from ..models import Post
from ..permissions import IsOwnerOrReadOnly
from ..serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
    UpdatePostsListSerializer,
)


@extend_schema_view(
    list=post_list_doc,
    retrieve=post_retrieve_doc,
    create=post_create_doc,
    destroy=post_delete_doc,
    update=post_update_doc,
    partial_update=post_patch_doc,
)
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    http_method_names = ["get", "post", "delete", "put", "patch"]
    serializer_class = GetPostsListSerializer
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    queryset = Post.objects.select_related("author").order_by("-date", "-id")

    def get_serializer_class(self):
        if self.action == "create":
            return CreatePostsListSerializer
        if self.action in ["update", "partial_update"]:
            return UpdatePostsListSerializer
        return GetPostsListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    