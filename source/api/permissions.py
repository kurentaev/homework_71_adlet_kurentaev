from rest_framework import permissions


class PermissionPolicyMixin:
    def check_permissions(self, request):
        try:
            handler = getattr(self, request.method.lower())
        except AttributeError:
            handler = None
        if (
            handler
            and self.permission_classes_per_method
            and self.permission_classes_per_method.get(handler.__name__)
        ):
            self.permission_classes = self.permission_classes_per_method.get(handler.__name__)

        super().check_permissions(request)


class IsWriteUser(permissions.BasePermission):
    def has_object_permission(self, request, view, post):
        if request.user == post.author:
            return True
        return False
