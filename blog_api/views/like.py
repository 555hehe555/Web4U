from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from rest_framework import permissions, status, mixins, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view

from documentation import like_list_doc, like_post_doc, like_delete_doc
from ..models import Like, Post
from ..pagination import LikePagination
from ..serializers import GetAllUserLikeSerializer, CreateUserLikeSerializer
from ..errors import LikeNotFound, DuplicateLike


@extend_schema_view(
    list=like_list_doc,
    create=like_post_doc,
    destroy=like_delete_doc
)
class LikePostViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    http_method_names = ["get", "post", "delete"]
    pagination_class = LikePagination
    serializer_class = GetAllUserLikeSerializer

    def get_post(self):
        post_pk = self.kwargs.get("post_pk")
        return get_object_or_404(Post, pk=post_pk)

    def get_queryset(self):
        post = self.get_post()
        return Like.objects.filter(post=post).select_related("user").order_by("-id")

    def get_permissions(self):
        if self.action == "list":
            return [permissions.AllowAny()]
        if self.action in ["create", "destroy"]:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserLikeSerializer
        return GetAllUserLikeSerializer

    def perform_create(self, serializer):
        post = self.get_post()

        if Like.objects.filter(user=self.request.user, post=post).exists():
            raise DuplicateLike()

        try:
            serializer.save(user=self.request.user, post=post)
        except IntegrityError:
            raise DuplicateLike()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        read_serializer = GetAllUserLikeSerializer(
            serializer.instance,
            context={"request": request},
        )
        return Response(read_serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        user_liked = (
            request.user.is_authenticated
            and queryset.filter(user=request.user).exists()
        )

        page = self.paginate_queryset(queryset)
        if page is not None:
            self.paginator.user_liked = user_liked
            serializer = self.get_serializer(
                page,
                many=True,
                context={"request": request},
            )
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(
            queryset,
            many=True,
            context={"request": request},
        )
        return Response({
            "count": queryset.count(),
            "next": None,
            "previous": None,
            "results": serializer.data,
            "user_liked": user_liked,
        })

    def destroy(self, request, *args, **kwargs):
        post = self.get_post()
        like = Like.objects.filter(user=request.user, post=post).first()

        if not like:
            raise LikeNotFound()

        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    