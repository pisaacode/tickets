from rest_framework import permissions


class TicketsPermission(permissions.BasePermission):

    group_name = "Soporte"

    def has_permission(self, request, view):
        try:
            request.user.groups.get(name=self.group_name)
            return True
        except Exception as e:
            return False
