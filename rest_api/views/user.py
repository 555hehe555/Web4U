from django.contrib.auth import authenticate, login, logout

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema_view

from documentation import login_user_list_doc, logout_user_list_doc, user_list_doc, post_list_doc, get_me_doc

from ..models import CustomUser, Post
from ..permissions import IsOwner
from ..serializers import (
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    DeleteCustomUserSerializer,
    PutCustomUserSerializer,
    PatchCustomUserSerializer,
    GetPostOneUserSerializer,
    LoginCustomUserSerializer,
    GetMeSerializer
)


@extend_schema_view(
    list=user_list_doc,
    retrieve=user_list_doc,
    create=user_list_doc,
    destroy=user_list_doc,
    update=user_list_doc,
    partial_update=user_list_doc,
    post_list=post_list_doc,
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


@extend_schema_view(me=get_me_doc)
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

