from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, permissions
from drf_spectacular.utils import extend_schema_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from documentation.comments import comments_list_doc
from documentation.likes import like_list_doc
from documentation.login_user import login_user_list_doc, logout_user_list_doc
from documentation.posts import post_list_doc
from documentation.custom_user import user_list_doc
from .models import Post, Comments, Like, CustomUser
from .permissions import IsOwner, IsOwnerOrReadOnly
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
    PatchCustomUserSerializer,
    GetMeSerializer,
    LoginCustomUserSerializer, GetPostOneUserSerializer
)
import colorama

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
    parser_classes = (MultiPartParser, FormParser)
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


@extend_schema_view(
    list=like_list_doc,
    retrieve=like_list_doc,
    create=like_list_doc,
    destroy=like_list_doc
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



@extend_schema_view(
    list=user_list_doc,
    retrieve=user_list_doc,
    create=user_list_doc,
    destroy=user_list_doc,
    update=user_list_doc,
    partial_update=user_list_doc
)
class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post', 'delete', 'put', 'patch']
    serializer_class = GetCustomUserSerializer
    queryset = CustomUser.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'create', 'post_list']:
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

        elif self.action == 'post_list':
            return GetPostOneUserSerializer
        return super().get_serializer_class()

    @action(detail=True, methods=['get'], url_path='posts')
    def post_list(self, request, user_pk=None):

        posts = Post.objects.filter(author_id=user_pk).order_by('-date')
        serializer = self.get_serializer(posts, many=True)

        return Response(serializer.data)


@extend_schema_view(me=login_user_list_doc)
class ManagerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=["get"], detail=False, url_path="me")
    def me(self, request):
        serializer = GetMeSerializer(self.request.user)
        return Response(serializer.data)


@extend_schema_view(login=login_user_list_doc,
                    logout=logout_user_list_doc)
class AuthViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = LoginCustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({"detail": "Invalid credentials"}, status=400)

        logout(request)  # закриває попередню сесію, якщо є
        login(request, user)
        return Response({"detail": "Login successful"})

    @action(detail=False, methods=["post"])
    def logout(self, request):
        logout(request)
        return Response({"detail": "Logout successful"})