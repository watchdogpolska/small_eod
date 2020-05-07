from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.urls import reverse
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserSerializer, User
from django.conf import settings
from .serializers import (
    RequestSerializer,
    TokenResponseSerializer,
    RefreshTokenRequestSerializer,
)
from requests_oauthlib import OAuth2Session
from rest_framework_simplejwt.tokens import RefreshToken

authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
token_url = "https://www.googleapis.com/oauth2/v4/token"
userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_oauthlib(self, request):
        return OAuth2Session(
            client_id=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            scope=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE,
            redirect_uri=request.build_absolute_uri(reverse("user-exchange")),
        )

    @swagger_auto_schema(
        method="get",
        operation_description="API endpoint to receive URI for OAuth authorization url",
        responses={200: RequestSerializer()},
        manual_parameters=[],
        security=[],
    )
    @action(detail=False)
    def auth(self, request):
        google = self.get_oauthlib(request)
        authorization_url, state = google.authorization_url(url=authorization_base_url)
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
        google = self.get_oauthlib(request)
        google.fetch_token(
            token_url=token_url,
            client_secret=settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            authorization_response=request.build_absolute_uri(),
        )
        resp = google.get(userinfo_url)
        profile = resp.json()
        user, _ = User.objects.get_or_create(
            defaults={
                "username": profile["email"],
                "first_name": profile["given_name"],
                "second_name": profile["family_name"],
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
