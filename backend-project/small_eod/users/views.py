from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, User
from django.conf import settings
from .serializers import (
    RequestSerializer,
    TokenResponseSerializer,
    RefreshTokenRequestSerializer,
)
from rest_framework_simplejwt.tokens import RefreshToken
from .providers import GoogleProvider


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    provider = GoogleProvider(
        client_id=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        client_secret=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        scopes=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE,
    )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    ]

    def get_permissions(self):
        if self.action in ["auth", "exchange", "refresh"]:
            return [
                AllowAny(),
            ]
        return super().get_permissions()

    @swagger_auto_schema(
        method="get",
        operation_description="API endpoint to receive URI for OAuth authorization url",
        responses={200: RequestSerializer()},
        manual_parameters=[],
        security=[],
    )
    @action(detail=False)
    def auth(self, request):
        authorization_url, state = self.provider.callback_url(request)
        request.session["state"] = state
        serializer = RequestSerializer({"url": authorization_url})
        return Response(serializer.data)

    @action(detail=False)
    @swagger_auto_schema(
        operation_description="API endpoint to exchange "
        + "authorization code to access token",
        responses={200: TokenResponseSerializer()},
        manual_parameters=[],
        security=[],
    )
    def exchange(self, request):
        profile = self.provider.exchange(request)
        user, _ = User.objects.get_or_create(
            defaults={
                "username": profile["email"],
                "first_name": profile["given_name"],
                "last_name": profile["family_name"],
                "email": profile["email"],
            },
            email=profile["email"],
        )
        refresh = RefreshToken.for_user(user)
        serializer = TokenResponseSerializer(
            {"refresh_token": str(refresh), "access_token": str(refresh.access_token)}
        )
        return Response(serializer.data)

    @action(detail=False, methods=["post"])
    @swagger_auto_schema(
        operation_description="API endpoint to exchange "
        + "refresh token to fresh access token",
        responses={200: TokenResponseSerializer()},
        request_body=RefreshTokenRequestSerializer,
        manual_parameters=[],
        security=[],
    )
    def refresh(self, request):
        serializer_input = RefreshTokenRequestSerializer(data=request.data)
        serializer_input.is_valid(raise_exception=True)
        refresh = RefreshToken(serializer_input.validated_data["refresh_token"])
        refresh.set_jti()
        refresh.set_exp()
        serializer = TokenResponseSerializer(
            {"refresh_token": str(refresh), "access_token": str(refresh.access_token)}
        )
        return Response(serializer.data)
