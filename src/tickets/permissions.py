from rest_framework.permissions import BasePermission
from tickets.models import Ticket
from users.constants import Role


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.ADMIN


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER


class IsUserOwner(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj: Ticket):
        return obj.customer == request.user


class IsManagerProcessing(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj: Ticket):
        return obj.manager == request.user


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER
