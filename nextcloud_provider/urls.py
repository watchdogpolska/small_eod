from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns

from .provider import NextcloudProvider


urlpatterns = default_urlpatterns(NextcloudProvider)
