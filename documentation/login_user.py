from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample, inline_serializer
from rest_framework import serializers, status

from blog_api.serializers import LoginCustomUserSerializer


MessageSerializer = inline_serializer(
    name="MessageResponse",
    fields={
        "detail": serializers.CharField(),
    },
)

login_user_list_doc = extend_schema(
    tags=["Auth"],
    description="Login API",
    request=LoginCustomUserSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=MessageSerializer,
            description="Login successful",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Login successful"},
                    response_only=True,
                    status_codes=[200],
                )
            ],
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response=MessageSerializer,
            description="Login failed",
            examples=[
                OpenApiExample(
                    name="Failed response",
                    value={"detail": "Invalid credentials"},
                    response_only=True,
                    status_codes=[400],
                )
            ],
        ),
    },
)

logout_user_list_doc = extend_schema(
    tags=["Auth"],
    description="Logout API",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=MessageSerializer,
            description="Logout successful",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={"detail": "Logout successful"},
                    response_only=True,
                    status_codes=[200],
                )
            ],
        )
    },
)
