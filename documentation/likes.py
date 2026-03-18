from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetAllUserLikeSerializer,
    CreateUserLikeSerializer,
)


like_list_doc = extend_schema(
    tags=['Like'],
    description="Like API",
    request=CreateUserLikeSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetAllUserLikeSerializer,
            description="List of likes",
            examples=[
                OpenApiExample(
                    name="List response",
                    value=[
                        {
                            "id": 1,
                            "user": 1,
                            "post": 1,
                            "created_at": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetAllUserLikeSerializer,
            description="Like created",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 2,
                        "user": 1,
                        "post": 2,
                        "created_at": "2026-03-18T16:05:00Z",
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
                    value={"post": ["This field is required."]},
                )
            ],
        ),
    },
)
