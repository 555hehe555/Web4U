from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status

from rest_api.serializers import LoginCustomUserSerializer


login_user_list_doc = extend_schema(
    tags=['Login'],
    description="Login API",
    request=LoginCustomUserSerializer,  # тіло запиту
    responses={
        status.HTTP_200_OK: OpenApiTypes.OBJECT,  # можна серіалізатор або OpenApiTypes
    },
)

logout_user_list_doc = extend_schema(
    tags=['Login'],
    description="Login API",
    request=None,  # тіло запиту
    responses={
        status.HTTP_200_OK: OpenApiTypes.NONE,  # можна серіалізатор або OpenApiTypes
    },
)