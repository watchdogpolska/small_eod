from rest_framework.permissions import BasePermission, SAFE_METHODS
from .signer import JWTSigner
import jwt
from django.urls import resolve

signer = JWTSigner()


class TokenPermission(BasePermission):
    def get_header(self, request):
        """
        Extracts the header containing the token from the given
        request.
        """
        return request.META.get("HTTP_AUTHORIZATION")

    def get_raw_token(self, header):
        """
        Extracts an unvalidated token from the given "Authorization"
        header value.
        """
        parts = header.split()

        if len(parts) == 0:
            return None

        if parts[0] != "Bearer":
            return None

        if len(parts) != 2:
            return None

        return parts[1]

    def has_object_permission(self, request, view, obj):
        """
        Validate request token for collection.
        """
        if request.method not in SAFE_METHODS:
            return False
        header = self.get_header(request)
        if not header:
            return False
        raw_token = self.get_raw_token(header)
        pk = self.get_collection_pk(request, view, obj)
        if not pk:  # not allow list collections
            return False
        except_subject = f"collection-{pk}"

        try:
            token = signer.unsign(payload=raw_token, request=request)
        except jwt.exceptions.InvalidTokenError:
            return False

        return except_subject == token["sub"]


class CollectionDirectTokenPermission(TokenPermission):
    def get_collection_pk(self, request, view, obj):
        func, args, kwargs = resolve(request.path)
        return kwargs.get("pk", None)

    def has_permission(self, request, view):
        return self.has_object_permission(request, view, None)


class CollectionMemberTokenPermission(TokenPermission):
    def get_collection_pk(self, request, view, obj):
        func, args, kwargs = resolve(request.path)
        return kwargs["collection_pk"]

    def has_permission(self, request, view):
        return self.has_object_permission(request, view, None)
