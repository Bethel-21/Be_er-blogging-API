
from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Allow read for everyone.
    Write only for object author or admin.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # admin users allowed
        if request.user and getattr(request.user, 'role', None) == 'admin':
            return True
        # object must have `author` attribute
        return hasattr(obj, 'author') and obj.author == request.user