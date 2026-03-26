from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from rest_api.serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
    DeletePostsListSerializer,
    PutPostsListSerializer,
    PatchPostsListSerializer,
)


post_list_doc = extend_schema(
    tags=['Posts'],
    description="Posts API - List and Retrieve",
    request=None,
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
                            "description": "This is the first post",
                            "author": "john_doe",
                            "img": "image_url",
                            "date": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
    },
)

post_create_doc = extend_schema(
    tags=['Posts'],
    description="Create Post API",
    request=CreatePostsListSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetPostsListSerializer,
            description="Post created successfully",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 2,
                        "title": "New post",
                        "description": "Content of the new post",
                        "author": "john_doe",
                        "img": "image_url",
                        "date": "2026-03-18T16:05:00Z",
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

post_update_doc = extend_schema(
    tags=['Posts'],
    description="Update Post API (full update)",
    request=PutPostsListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetPostsListSerializer,
            description="Post updated successfully",
            examples=[
                OpenApiExample(
                    name="Updated response",
                    value={
                        "id": 1,
                        "title": "Updated title",
                        "description": "Updated description",
                        "img": "new_image_url",
                        "author": "john_doe",
                        "date": "2026-03-18T16:10:00Z",
                    },
                )
            ],
        ),
        status.HTTP_400_BAD_REQUEST: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Invalid data",
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Post not found",
        ),
    },
)

post_patch_doc = extend_schema(
    tags=['Posts'],
    description="Partial Update Post API",
    request=PatchPostsListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetPostsListSerializer,
            description="Post partially updated successfully",
            examples=[
                OpenApiExample(
                    name="Patched response",
                    value={
                        "id": 1,
                        "title": "Updated title",
                        "description": "Original description",
                        "img": "image_url",
                        "author": "john_doe",
                        "date": "2026-03-18T16:10:00Z",
                    },
                )
            ],
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Post not found",
        ),
    },
)

post_delete_doc = extend_schema(
    tags=['Posts'],
    description="Delete Post API",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="Post deleted successfully",
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Post not found",
        ),
    },
)
