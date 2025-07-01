from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_api.serializers import GetCommentListSerializer


comments_list_doc = extend_schema(
    tags=['Comments'],
    description="Comments API",
    responses={
        status.HTTP_200_OK: GetCommentListSerializer
    },
)
