from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, inline_serializer
from rest_framework import serializers, status

from blog_api.serializers import LoginCustomUserSerializer


login_user_list_doc = extend_schema(
    tags=["Auth"],
    description="Login user.",
    request=LoginCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=inline_serializer(
                name="LoginSuccessResponse",
                fields={
                    "detail": serializers.CharField(),
                },
            ),
            description="Login successful.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Login successful"},
                    response_only=True,
                )
            ],
        ),
    },
)

logout_user_list_doc = extend_schema(
    tags=["Auth"],
    description="Logout current user.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=inline_serializer(
                name="LogoutSuccessResponse",
                fields={
                    "detail": serializers.CharField(),
                },
            ),
            description="Logout successful.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Logout successful"},
                    response_only=True,
                )
            ],
        ),
    },
)
