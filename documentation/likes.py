from drf_spectacular.utils import extend_schema, OpenApiResponse, OpenApiExample
from rest_framework import status

from blog_api.serializers import (
    GetAllUserLikeSerializer,
    LikePaginatedResponseSerializer,
)

like_list_doc = extend_schema(
    tags=["Like"],
    description="Get paginated likes for the selected post.",
    request=None,
    responses={
        status.HTTP_200_OK: OpenApiResponse(
            response=LikePaginatedResponseSerializer,
            description="Paginated likes list.",
            examples=[
                OpenApiExample(
                    name="Success response",
                    value={
                        "count": 57,
                        "next": "http://127.0.0.1:8000/api/posts/6/likes/?page=2",
                        "previous": None,
                        "results": [
                            {
                                "id": 9,
                                "author": "admin",
                                "post": 6,
                            }
                        ],
                        "user_liked": True,
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

like_post_doc = extend_schema(
    tags=["Like"],
    description="Create like for the selected post.",
    request=None,
    responses={
        status.HTTP_201_CREATED: OpenApiResponse(
            response=GetAllUserLikeSerializer,
            description="Like created successfully.",
            examples=[
                OpenApiExample(
                    name="Created response",
                    value={
                        "id": 9,
                        "author": "admin",
                        "post": 6,
                    },
                    response_only=True,
                )
            ],
        ),
    },
)

like_delete_doc = extend_schema(
    tags=["Like"],
    description="Delete current user's like from the selected post.",
    request=None,
    responses={
        status.HTTP_204_NO_CONTENT: OpenApiResponse(
            response=None,
            description="Like deleted successfully.",
        ),
    },
)
