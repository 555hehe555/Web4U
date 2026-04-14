from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status

from blog_api.serializers import (
    GetPostsListSerializer,
    CreatePostsListSerializer,
    UpdatePostsListSerializer,
)


post_list_doc = extend_schema(
    tags=["Posts"],
    description="Get paginated list of posts.",
    request=None,
    responses={
        status.HTTP_200_OK: GetPostsListSerializer(many=True),
    },
)

post_retrieve_doc = extend_schema(
    tags=["Posts"],
    description="Get post details by id.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetPostsListSerializer,
            description="Post details.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={
                        "id": 6,
                        "title": "My first post",
                        "description": "Post description text",
                        "img": "/media/image/temp/2026/example.jpg",
                        "author": "admin",
                        "date": "2026-04-14T12:00:00Z",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

post_create_doc = extend_schema(
    tags=["Posts"],
    description="Create post.",
    request=CreatePostsListSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=CreatePostsListSerializer,
            description="Post created successfully.",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "title": "New post",
                        "description": "New description",
                        "img": "/media/image/temp/2026/example.jpg",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

post_update_doc = extend_schema(
    tags=["Posts"],
    description="Fully update post.",
    request=UpdatePostsListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UpdatePostsListSerializer,
            description="Post updated successfully.",
            examples=[
                OpenApiExample(
                    name="Updated response",
                    value={
                        "title": "Updated post",
                        "description": "Updated description",
                        "img": "/media/image/temp/2026/example.jpg",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

post_patch_doc = extend_schema(
    tags=["Posts"],
    description="Partially update post.",
    request=UpdatePostsListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=UpdatePostsListSerializer,
            description="Post partially updated successfully.",
            examples=[
                OpenApiExample(
                    name="Patched response",
                    value={
                        "title": "Patched post",
                        "description": "Patched description",
                        "img": "/media/image/temp/2026/example.jpg",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

post_delete_doc = extend_schema(
    tags=["Posts"],
    description="Delete post.",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="Post deleted successfully.",
        ),
    },
)
