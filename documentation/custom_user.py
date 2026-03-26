from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    DeleteCustomUserSerializer,
    PutCustomUserSerializer,
    PatchCustomUserSerializer,
    GetMeSerializer,
    GetPostOneUserSerializer,
)


user_list_doc = extend_schema(
    tags=['User'],
    description="User API - List and Retrieve users",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="List of users",
            examples=[
                OpenApiExample(
                    name="List response",
                    value=[
                        {
                            "id": 1,
                            "username": "aboba",
                            "email": "aboba@example.com",
                            "first_name": "aboba",
                            "last_name": "aboba",
                            "is_active": True,
                            "is_staff": False,
                            "is_superuser": False,
                        }
                    ],
                )
            ],
        ),
    },
)

user_create_doc = extend_schema(
    tags=['User'],
    description="Create User API",
    request=CreateCustomUserSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User created successfully",
            examples=[
                OpenApiExample(
                    name="Created user",
                    value={
                        "id": 2,
                        "username": "newuser",
                        "email": "newuser@example.com",
                        "first_name": "New",
                        "last_name": "User",
                        "is_active": True,
                    },
                )
            ],
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Invalid data",
            examples=[
                OpenApiExample(
                    name="Bad request",
                    value={"username": ["This field is required."]},
                )
            ],
        ),
    },
)

user_update_doc = extend_schema(
    tags=['User'],
    description="Update User API (full update)",
    request=PutCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User updated successfully",
            examples=[
                OpenApiExample(
                    name="Updated user",
                    value={
                        "id": 1,
                        "username": "updated_user",
                        "email": "updated@example.com",
                        "first_name": "Updated",
                        "last_name": "User",
                    },
                )
            ],
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="User not found",
        ),
    },
)

user_patch_doc = extend_schema(
    tags=['User'],
    description="Partial Update User API",
    request=PatchCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User partially updated successfully",
            examples=[
                OpenApiExample(
                    name="Patched user",
                    value={
                        "id": 1,
                        "username": "aboba",
                        "email": "newemail@example.com",
                        "first_name": "aboba",
                        "last_name": "updated_last_name",
                    },
                )
            ],
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="User not found",
        ),
    },
)

user_delete_doc = extend_schema(
    tags=['User'],
    description="Delete User API",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="User deleted successfully",
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="User not found",
        ),
    },
)

post_list_doc = extend_schema(
    tags=['User'],
    description="Get User Posts API",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetPostOneUserSerializer,
            description="List of user's posts",
            examples=[
                OpenApiExample(
                    name="User posts response",
                    value=[
                        {
                            "id": 1,
                            "title": "First post",
                            "description": "Post description",
                            "author": "aboba",
                            "img": "image_url",
                            "date": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
    },
)

get_me_doc = extend_schema(
    tags=['User'],
    description="Get current authenticated user",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetMeSerializer,
            description="Current authenticated user details",
            examples=[
                OpenApiExample(
                    name="Current user",
                    value={
                        "id": 1,
                        "username": "aboba",
                        "email": "aboba@example.com",
                        "is_staff": False,
                        "is_superuser": False,
                        "date_joined": "2026-03-18T15:41:15Z",
                        "last_login": "2026-03-18T16:04:51Z",
                        "is_active": True,
                        "first_name": "aboba",
                        "last_name": "aboba",
                        "password": "pbkdf2_sha256$720000$aboba..."
                    },
                )
            ],
        ),
        status.HTTP_401_UNAUTHORIZED: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Unauthorized",
            examples=[
                OpenApiExample(
                    name="Unauthorized",
                    value={"detail": "Authentication credentials were not provided."},
                )
            ],
        ),
    },
)
