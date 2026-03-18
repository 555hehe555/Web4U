from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetCustomUserSerializer,
    CreateCustomUserSerializer,
    GetMeSerializer,
)


user_list_doc = extend_schema(
    tags=['User'],
    description="User API",
    request=CreateCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User details",
            examples=[
                OpenApiExample(
                    name="Get user",
                    value={
                        "id": 1,
                        "username": "aboba",
                        "email": "aboba@example.com",
                        "first_name": "aboba",
                        "last_name": "aboba",
                    },
                )
            ],
        ),
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetCustomUserSerializer,
            description="User created",
            examples=[
                OpenApiExample(
                    name="Created user",
                    value={
                        "id": 2,
                        "username": "newuser",
                        "email": "newuser@example.com",
                        "first_name": "New",
                        "last_name": "User",
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

get_me_doc = extend_schema(
    tags=['User'],
    description="Get current authenticated user",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetMeSerializer,
            description="Current user",
            examples=[
                OpenApiExample(
                    name="Current user",
                    value={
                        "id": 1,
                        "username": "aboba",
                        "email": "aboba@example.com",
                        "is_active": True,
                    },
                )
            ],
        )
    },
)
