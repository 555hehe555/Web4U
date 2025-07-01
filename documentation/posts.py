from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_api.serializers import GetPostsListSerializer


post_list_doc = extend_schema(
    tags=['Posts'],
    description="Posts API",
    responses={
        status.HTTP_200_OK: GetPostsListSerializer
    },
)
