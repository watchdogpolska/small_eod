from rest_framework.permissions import BasePermission, SAFE_METHODS
from .signer import JWTSigner
import jwt
from django.urls import resolve

signer = JWTSigner()


class TokenPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        Validate request token for collection.
        """
        if request.method not in SAFE_METHODS:
            return False

        try:
            raw_token = request.GET["authorization"]
        except KeyError:
            return False

        pk = self.get_collection_pk(request, view, obj)
        if not pk:  # not allow list collections
            return False

        try:
            token = signer.unsign(payload=raw_token, request=request)
        except jwt.exceptions.InvalidTokenError:
            return False

        except_subject = f"collection-{pk}"
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
