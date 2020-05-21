# Authentication

The application supports authentication with OAuth 2.0 identity provider.

## Flow

1. Authentication implements the OAuth protocol as a "Client Server". See [OAuth2 simply explained](https://aaronparecki.com/articles/2012/07/29/1/oauth2-simplified) or [full spec](https://oauth.net/2/) for detailed information.

2. Frontend fetch URI from `http://localhost:8000/api/users/auth/`.

3. Users agents should be redirect according to ```url```.

4. Backend is redirecting request to Google with proper setup based on `base.py` settings:
    - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

    A long with these settings request contains redirect URI to `http://localhost:8000/api/users/exchange` and random characters to identify state.

    Example URL to where user will be redirected:
    `https://accounts.google.com/o/oauth2/auth?client_id=key&redirect_uri=http://localhost:8000/api/auth/complete/google-oauth2/&state=YkxuVMTmx4Diw1gzD3EgcRuDY6k7id4D&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid+email+profile`

5. User authorizes `small_eod` application.
6. Google uses `redirect_uri` and make request with authorization code.

    Example callback URI:
    `http://localhost:8000/api/auth/exchange/?code=4/ygHGt7j39aW2i17VRynVIDVILasdasdNfMQa4KCE-XUead4IM0ulU8ffDVlRHHFrtWqgbqWhQCCYv0ORFG7_7BM`

7. Backend receives request with authorization code
   and exchanges it for Google access, create local user account and provide access token.

8. Front-end periodically refresh access token by request to ```/api/auth/refresh```.

9. Front-end pass access token in ```Authorization: Bearer <token>``` header.

    ```bash
    $ curl -H "Authorization: Bearer google-oauth2 <access_token>" http://localhost:8000/api/cases/
    {'count': 0, 'next': None, 'previous': None, 'results': []}
    ```
