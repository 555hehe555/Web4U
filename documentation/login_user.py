from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status

from rest_api.serializers import LoginCustomUserSerializer


login_user_list_doc = extend_schema(
    tags=['Auth'],
    description="Login API",
    request=LoginCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=True,
            description="Login successful",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Login successful"},
                )
            ],
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response=True,
            description="Login failed",
            examples=[
                OpenApiExample(
                    name="Failed response",
                    value={"detail": "Invalid credentials"},
                )
            ],
        )
    },
)

logout_user_list_doc = extend_schema(
    tags=['Auth'],
    description="Logout API",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=True,
            description="Logout successful",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Logout successful"},
                )
            ],
        )
    },
)

get_me_doc = extend_schema(
    tags=['Auth'],
    description="Get current info API",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=True,
            description="Get successful",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={
                      "id": 1,
                      "username": "aboba",
                      "email": "aboba@example.com",
                      "is_staff": False,
                      "is_superuser": True,
                      "date_joined": "3026-31-13T15:41:15.847892Z",
                      "last_login": "2026-03-18T16:04:51.184195Z",
                      "is_active": True,
                      "first_name": "abobaaboba",
                      "last_name": "abobaabobaaboba",
                      "password": "pbkdf2_sha256$720000$aboba@aboba#aboba%aboba^aboba&aboba*aboba(aboba)aboba!aboba"
                    },
                )
            ],
        )
    },
)
