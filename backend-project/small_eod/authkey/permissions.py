from rest_framework import permissions
from .models import Key
from .parser import get_token


class AuthKeyPermission(permissions.BasePermission):
    def get_required_scopes(self, view):
        if hasattr(view, "required_scopes_map") and hasattr(view, "name"):
            return view.required_scopes_map.get(
                view.name, getattr(view, "required_scopes", [])
            )
        return getattr(view, "required_scopes", [])

    def has_permission(self, request, view):
        token = get_token(request)
        if not token:
            return False
        key = Key.objects.get(token=token)
        scopes = self.get_required_scopes(view)
        return key.has_scopes(scopes)
