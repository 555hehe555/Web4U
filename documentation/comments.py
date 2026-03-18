from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetCommentListSerializer,
    CreateCommentListSerializer,
)


comments_list_doc = extend_schema(
    tags=['Comments'],
    description="Comments API",
    request=CreateCommentListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCommentListSerializer,
            description="List of comments",
            examples=[
                OpenApiExample(
                    name="List response",
                    value=[
                        {
                            "id": 1,
                            "post": 1,
                            "author": 1,
                            "content": "Nice post!",
                            "created_at": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetCommentListSerializer,
            description="Comment created",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 2,
                        "post": 1,
                        "author": 1,
                        "content": "Another comment",
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
                    value={"content": ["This field is required."]},
                )
            ],
        ),
    },
)
