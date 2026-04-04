from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample

from rest_framework import status

from blog_api.serializers import (
    GetCommentListSerializer,
    CreateCommentListSerializer,
    DeleteCommentListSerializer,
    PutCommentListSerializer,
    PatchCommentListSerializer,
)


comments_list_doc = extend_schema(
    tags=['Comments'],
    description="Comments API - List and Retrieve",
    request=None,
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
                            "text_comments": "Nice post!",
                            "user": "john_doe",
                            "post": 1,
                            "date": "2026-03-18T16:00:00Z",
                        }
                    ],
                )
            ],
        ),
    },
)

comments_create_doc = extend_schema(
    tags=['Comments'],
    description="Create Comment API",
    request=CreateCommentListSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetCommentListSerializer,
            description="Comment created successfully",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 2,
                        "text_comments": "Another comment",
                        "user": "jane_doe",
                        "post": 1,
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
                    value={"text_comments": ["This field is required."]},
                )
            ],
        ),
    },
)

comments_update_doc = extend_schema(
    tags=['Comments'],
    description="Update Comment API (full update)",
    request=PutCommentListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCommentListSerializer,
            description="Comment updated successfully",
            examples=[
                OpenApiExample(
                    name="Updated response",
                    value={
                        "id": 1,
                        "text_comments": "Updated comment text",
                        "user": "john_doe",
                        "post": 1,
                        "date": "2026-03-18T16:10:00Z",
                    },
                )
            ],
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Comment not found",
        ),
    },
)

comments_patch_doc = extend_schema(
    tags=['Comments'],
    description="Partial Update Comment API",
    request=PatchCommentListSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=GetCommentListSerializer,
            description="Comment partially updated successfully",
            examples=[
                OpenApiExample(
                    name="Patched response",
                    value={
                        "id": 1,
                        "text_comments": "Updated comment text",
                        "user": "john_doe",
                        "post": 1,
                        "date": "2026-03-18T16:05:00Z",
                    },
                )
            ],
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Comment not found",
        ),
    },
)

comments_delete_doc = extend_schema(
    tags=['Comments'],
    description="Delete Comment API",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="Comment deleted successfully",
        ),
        status.HTTP_404_NOT_FOUND: OpenApiResponse(
            response=OpenApiTypes.OBJECT,
            description="Comment not found",
        ),
    },
)
