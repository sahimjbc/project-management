from rest_framework.permissions import BasePermission

class HasMenuPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        required_menu = getattr(view, 'menu', None)
        required_action = getattr(view, 'action', None)

        if not required_menu or not required_action:
            return True

        if user.is_superuser:
            return True

        if not user.role:
            return False

        return user.role.permissions.filter(menu=required_menu, action=required_action).exists()
