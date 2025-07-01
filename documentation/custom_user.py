from drf_spectacular.utils import extend_schema
from rest_framework import status

from rest_api.serializers import GetCustomUserSerializer


user_list_doc = extend_schema(
    tags=['User'],
    description="User API",
    responses={
        status.HTTP_200_OK: GetCustomUserSerializer
    },
)
