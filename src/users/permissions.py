from rest_framework.permissions import BasePermission
from users.constants import Role


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN
