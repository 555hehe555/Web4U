from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view
from rest_framework.exceptions import AuthenticationFailed

from documentation import (
    login_user_list_doc,
    logout_user_list_doc,
    user_list_doc,
    user_post_list_doc,
    user_retrieve_doc,
    user_create_doc,
    user_update_doc,
    user_patch_doc,
    user_delete_doc,
    get_me_doc,
)

from ..models import CustomUser, Post
from ..permissions import IsOwnerOrAdminDelete
from ..serializers import (
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    UpdateCustomUserSerializer,
    GetPostOneUserSerializer,
    LoginCustomUserSerializer,
    GetMeSerializer
)


@extend_schema_view(
    list=user_list_doc,
    retrieve=user_retrieve_doc,
    create=user_create_doc,
    destroy=user_delete_doc,
    update=user_update_doc,
    partial_update=user_patch_doc,
    post_list=user_post_list_doc,
)
class CustomUserViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "post", "delete", "put", "patch"]
    serializer_class = GetCustomUserSerializer
    queryset = CustomUser.objects.all().order_by("-date_joined", "-id")

    def get_permissions(self):
        if self.action in ["list", "retrieve", "create", "post_list"]:
            return [permissions.AllowAny()]
        return [IsOwnerOrAdminDelete()]

    def get_serializer_class(self):
        if self.action == "create":
            return CreateCustomUserSerializer
        if self.action in ["update", "partial_update"]:
            return UpdateCustomUserSerializer
        if self.action == "post_list":
            return GetPostOneUserSerializer
        return GetCustomUserSerializer

    @action(detail=True, methods=["get"], url_path="posts")
    def post_list(self, request, *args, **kwargs):
        user_pk = self.kwargs.get("user_pk")

        posts = Post.objects.filter(author_id=user_pk).order_by("-date", "-id")

        # page = self.paginate_queryset(posts)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)
        
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


@extend_schema_view(me=get_me_doc)
class ManagerViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @action(methods=["get"], detail=False, url_path="me")
    def me(self, request):
        serializer = GetMeSerializer(request.user) 
        return Response(serializer.data)


@extend_schema_view(
    login=login_user_list_doc,
    logout=logout_user_list_doc,
)
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
            raise AuthenticationFailed(detail="Invalid credentials.", code="invalid_credentials")

        django_logout(request)
        django_login(request, user)
        return Response({"detail": "Login successful"})

    @action(detail=False, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def logout(self, request):
        django_logout(request)
        return Response({"detail": "Logout successful"})
