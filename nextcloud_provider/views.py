from urllib.parse import urljoin

from django.core.exceptions import PermissionDenied

# Create your views here.
import requests

from allauth.socialaccount.providers.oauth2.views import (
    OAuth2Adapter,
    OAuth2CallbackView,
    OAuth2LoginView,
)

from .provider import NextcloudProvider


class NextcloudOAuth2Adapter(OAuth2Adapter):
    provider_id = NextcloudProvider.id
    supports_state = False
    redirect_uri_protocol = 'https'
    required_group = None

    @property
    def instance_url(self):
        settings = self.get_provider().get_settings()
        return settings.get('INSTANCE_URL', 'https://dyski.siecobywatelska.pl')

    @property
    def authorize_url(self):
        return urljoin(self.instance_url, '/apps/oauth2/authorize')

    @property
    def profile_url(self):
        return urljoin(self.instance_url, '/ocs/v2.php/cloud/user?format=json')

    @property
    def access_token_url(self):
        return urljoin(self.instance_url, '/apps/oauth2/api/v1/token')

    def has_required_group(self, groups):
        settings = self.get_provider().get_settings()
        required_group = settings.get('REQUIRED_GROUP', None)
        if not required_group:
            return True
        return self.required_group in groups

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        response = requests.get(self.profile_url, headers=headers)
        extra_data = response.json()['ocs']['data']

        if not extra_data['enabled'] or not self.has_required_group(extra_data['groups']):
            raise PermissionDenied("You don't have right to use that app!")
        return self.get_provider().sociallogin_from_response(
            request,
            extra_data)


oauth2_login = OAuth2LoginView.adapter_view(NextcloudOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(NextcloudOAuth2Adapter)
