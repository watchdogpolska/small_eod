from requests_oauthlib import OAuth2Session


class GoogleProvider:
    authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    token_url = "https://www.googleapis.com/oauth2/v4/token"
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    def __init__(self, client_id, client_secret, scopes):
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes

    def get_oauthlib(self, request):
        return OAuth2Session(
            client_id=self.client_id,
            scope=self.scopes,
            redirect_uri=request.build_absolute_uri("/login/callback"),
        )

    def callback_url(self, request):
        google = self.get_oauthlib(request)
        return google.authorization_url(url=self.authorization_base_url)

    def exchange(self, request):
        google = self.get_oauthlib(request)
        google.fetch_token(
            token_url=self.token_url,
            client_secret=self.client_secret,
            authorization_response=request.build_absolute_uri(),
        )
        resp = google.get(self.userinfo_url)
        return resp.json()


class FakeProvider:
    base_url = "https://localhost:5678"

    def __init__(self, *args, **kwargs):
        pass

    def callback_url(self, request):
        # Hardcode localhost - the provider is expected to be used only in local deployments.
        # `build_absolute_uri` doesn't work, because it produces a docker friendly url.
        redirect_uri = f"http://localhost:8000/login/callback"
        return f"{self.base_url}?redirect_uri={redirect_uri}", None

    def exchange(self, request):
        # Hardcoded values.
        # Simple, but working.
        return {'email': "email@example.com", 'given_name': "GivenName", 'family_name': "FamilyName"}
