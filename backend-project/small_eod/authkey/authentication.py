from rest_framework import authentication
from rest_framework import exceptions
from .models import Key
from .parser import get_token


class AuthKeyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = get_token(request)
        if not token:
            return None
        try:
            key = Key.objects.select_related("user").get(token=token)
            user = key.user
        except Key.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid authentication token")
        key.update_used_on()
        return (user, None)
