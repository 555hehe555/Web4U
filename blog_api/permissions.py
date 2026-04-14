from rest_framework import permissions


def get_owner(obj):
    if hasattr(obj, "author"):
        return obj.author
    if hasattr(obj, "user"):
        return obj.user
    return obj


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return get_owner(obj) == request.user


class IsOwnerOrAdminDelete(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method == "DELETE" and request.user.is_staff:
            return True
        return get_owner(obj) == request.user
