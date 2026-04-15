from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from blog_api.serializers import (
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    UpdateCustomUserSerializer,
    GetPostOneUserSerializer,
    GetMeSerializer,
)


user_list_doc = extend_schema(
    tags=["Users"],
    description="Get paginated list of users.",
    request=None,
    responses={
        status.HTTP_200_OK: GetCustomUserSerializer(many=True),
    },
)

user_retrieve_doc = extend_schema(
    tags=["Users"],
    description="Get user details by id.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User details.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={
                        "id": 4,
                        "username": "admin",
                        "email": "admin@example.com",
                        "date_joined": "2026-04-14T12:00:00Z",
                        "first_name": "Admin",
                        "last_name": "User",
                        "last_login": "2026-04-14T13:00:00Z",
                        "is_active": True,
                        "is_staff": True,
                        "is_superuser": True,
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

user_create_doc = extend_schema(
    tags=["Users"],
    description="Create user.",
    request=CreateCustomUserSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=CreateCustomUserSerializer,
            description="User created successfully.",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 5,
                        "username": "new_user",
                        "email": "new_user@example.com",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

user_update_doc = extend_schema(
    tags=["Users"],
    description="Fully update user.",
    request=UpdateCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UpdateCustomUserSerializer,
            description="User updated successfully.",
            examples=[
                OpenApiExample(
                    name="Updated response",
                    value={
                        "username": "updated_user",
                        "email": "updated@example.com",
                        "first_name": "Updated",
                        "last_name": "User",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

user_patch_doc = extend_schema(
    tags=["Users"],
    description="Partially update user.",
    request=UpdateCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UpdateCustomUserSerializer,
            description="User partially updated successfully.",
            examples=[
                OpenApiExample(
                    name="Patched response",
                    value={
                        "username": "patched_user",
                        "email": "patched@example.com",
                        "first_name": "Patched",
                        "last_name": "User",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

user_delete_doc = extend_schema(
    tags=["Users"],
    description="Delete user.",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="User deleted successfully.",
        ),
    },
)

user_post_list_doc = extend_schema(
    tags=["Users"],
    description="Get paginated list of posts created by the selected user.",
    request=None,
    responses={
        status.HTTP_200_OK: GetPostOneUserSerializer(many=True),
    },
)

get_me_doc = extend_schema(
    tags=["Users"],
    description="Get current authenticated user.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetMeSerializer,
            description="Current user details.",
        ),
    },
)
