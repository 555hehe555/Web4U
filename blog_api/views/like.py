from rest_framework import viewsets, permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view

from documentation import like_list_doc, like_post_doc, like_delete_doc

from ..models import Like
from ..permissions import IsOwnerOrReadOnly
from ..serializers import GetAllUserLikeSerializer, CreateUserLikeSerializer, DeleteUserLikeSerializer

@extend_schema_view(
    list=like_list_doc,
    retrieve=like_list_doc,
    create=like_post_doc,
    destroy=like_delete_doc
)
class LikePostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    serializer_class = GetAllUserLikeSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get("post_pk")  # id поста з url
        return Like.objects.filter(post_id=post_pk)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        elif self.action in ['create', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'list':
            return GetAllUserLikeSerializer
        elif self.action == 'create':
            return CreateUserLikeSerializer
        elif self.action == 'destroy':
            return DeleteUserLikeSerializer
        return super().get_serializer_class()

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")  # id поста з url
        serializer.save(
            user_id=self.request.user.id,
            post_id=post_pk
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'request': request})

        data = {
            "count": queryset.count(),
            "results": serializer.data,
            "user_liked": (
                request.user.is_authenticated
                and queryset.filter(user_id=request.user.id).exists()
            )
        }
        return Response(data)
    
    def destroy(self, request, *args, **kwargs):
        post_pk = self.kwargs.get("post_pk")
        like = Like.objects.filter(
            user_id=request.user.id,
            post_id=post_pk
        ).first()
        if like:
            like.delete()
            return Response({"detail": "Like deleted successfully"}, status=204)
        return Response({"detail": "Like not found"}, status=404)
