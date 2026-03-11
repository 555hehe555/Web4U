from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read - everyone
    Write - only owner
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if hasattr(obj, "author"):
            return obj.author == request.user

        if hasattr(obj, "user"):
            return obj.user == request.user

        return False


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "author"):
            return obj.author == request.user

        if hasattr(obj, "user"):
            return obj.user == request.user

        return False


class IsAuthenticated(permissions.BasePermission):
    """
    Only authenticated users allowed
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated


class IsThisUser(permissions.BasePermission):
    """
    User can access only his own profile
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user
