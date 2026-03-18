from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
)


post_list_doc = extend_schema(
    tags=['Posts'],
    description="Posts API",
    request=CreatePostsListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetPostsListSerializer,
            description="List of posts",
            examples=[
                OpenApiExample(
                    name="List response",
                    value=[
                        {
                            "id": 1,
                            "title": "First post",
                            "content": "This is the first post",
                            "author": 1,
                            "created_at": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetPostsListSerializer,
            description="Post created",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 2,
                        "title": "New post",
                        "content": "Content of the new post",
                        "author": 1,
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
                    value={"title": ["This field is required."]},
                )
            ],
        ),
    },
)
