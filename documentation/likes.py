from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_api.serializers import GetAllUserLikeSerializer


like_list_doc = extend_schema(
    tags=['Like'],
    description="Like API",
    responses={
        status.HTTP_200_OK: GetAllUserLikeSerializer
    },
)
