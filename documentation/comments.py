from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status

from blog_api.serializers import (
    CommentReadSerializer,
    CommentCreateSerializer,
    CommentUpdateSerializer,
)


comments_list_doc = extend_schema(
    tags=["Comments"],
    description="Get paginated list of comments for the selected post.",
    request=None,
    responses={
        status.HTTP_200_OK: CommentReadSerializer(many=True),
    },
)

comments_retrieve_doc = extend_schema(
    tags=["Comments"],
    description="Get comment details by id for the selected post.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=CommentReadSerializer,
            description="Comment details.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={
                        "id": 15,
                        "text_comments": "string",
                        "user": "admin",
                        "post": 6,
                        "date": "2026-04-14T13:59:00.397897Z",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

comments_create_doc = extend_schema(
    tags=["Comments"],
    description="Create comment for the selected post.",
    request=CommentCreateSerializer,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=CommentReadSerializer,
            description="Comment created successfully.",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 16,
                        "text_comments": "New comment text",
                        "user": "admin",
                        "post": 6,
                        "date": "2026-04-14T14:10:00Z",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

comments_update_doc = extend_schema(
    tags=["Comments"],
    description="Fully update comment.",
    request=CommentUpdateSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=CommentReadSerializer,
            description="Comment updated successfully.",
            examples=[
                OpenApiExample(
                    name="Updated response",
                    value={
                        "id": 15,
                        "text_comments": "Updated comment text",
                        "user": "admin",
                        "post": 6,
                        "date": "2026-04-14T13:59:00.397897Z",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

comments_patch_doc = extend_schema(
    tags=["Comments"],
    description="Partially update comment.",
    request=CommentUpdateSerializer,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=CommentReadSerializer,
            description="Comment partially updated successfully.",
            examples=[
                OpenApiExample(
                    name="Patched response",
                    value={
                        "id": 15,
                        "text_comments": "Patched comment text",
                        "user": "admin",
                        "post": 6,
                        "date": "2026-04-14T13:59:00.397897Z",
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

comments_delete_doc = extend_schema(
    tags=["Comments"],
    description="Delete comment.",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="Comment deleted successfully.",
        ),
    },
)
