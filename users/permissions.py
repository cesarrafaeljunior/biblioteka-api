from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsCollaboratorOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_collaborator or obj == request.user
