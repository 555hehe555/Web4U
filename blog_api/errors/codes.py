from enum import StrEnum

class ErrorCode(StrEnum):
    LIKE_NOT_FOUND = "like_not_found"
    DUPLICATE_LIKE = "like_already_exists"
