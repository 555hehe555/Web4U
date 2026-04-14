from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError

from .codes import ErrorCode
from .messages import ErrorMessage


class LikeNotFound(NotFound):
    default_detail = ErrorMessage.LIKE_NOT_FOUND
    default_code = ErrorCode.LIKE_NOT_FOUND


class DuplicateLike(ValidationError):
    default_detail = ErrorMessage.DUPLICATE_LIKE
    default_code = ErrorCode.DUPLICATE_LIKE
