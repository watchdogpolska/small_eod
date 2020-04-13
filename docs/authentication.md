# Authentication

## Access token to internal application

### Obtaining access token

To obtain access token you have to make POST request to `http://localhost:8000/api/auth/token`, like that:
```python
import requests

response = requests.post("http://localhost:8000/api/auth/token", json={
    "client_id": "<client_id>", 
    "client_secret": "<client_secret>",
    "grant_type": "password", 
    "username": "<user_name>", 
    "password": "<user_password>",
})
print(response.json())
"""out:
{'accessToken': '4ASmIHyFZbWGaWiajRPb09VTX2jgBS',
 'expiresIn': 36000,
 'tokenType': 'Bearer',
 'scope': 'read write',
 'refreshToken': 'EbwvibhI7mLv7q3lQnfFRIPNcqLgbh'}
"""
```
or
```bash
$ curl \
    -H "Content-type: application/json" \
    -X POST -d \
    '{"client_id": "<client_id>", "client_secret": "<client_secret>", "grant_type": "password", "username": "<user_name>", "password": "<user_password>"}' \
    http://localhost:8000/api/auth/token
{"accessToken":"G0YmYgzOZZqspD9EbXIvmTc7EhqTkP","expiresIn":36000,"tokenType":"Bearer","scope":"read write","refreshToken":"1k4yu9HmBzMXT5nESWYS1BiYvWNfzj"}
```

### Authenticating request

Obtained `accessToken` we can use to authenticate request, by placing token into authorization header field:
```python
import requests

response = requests.get("http://localhost:8000/api/cases/", headers={"Authorization": "Bearer <access_token>"})
print(response, response.json())
"""out:
<Response [200]>
{'count': 0, 'next': None, 'previous': None, 'results': []}
"""
```
or
```bash
$ curl -H "Authorization: Bearer <access_token>" http://localhost:8000/api/cases/
{'count': 0, 'next': None, 'previous': None, 'results': []}
```
### Refreshing token

If our `accessToken` is nearly to be expired. We can obtain new one by using `refreshToken` and `http://localhost:8000/api/auth/token` endpoint:
```python
import requests

response = requests.post("http://localhost:8000/api/auth/token", json={
    "client_id": "<client_id>", 
    "client_secret": "<client_secret>",
    "grant_type": "refresh_token", 
    "refresh_token": "<refresh_token>",
})
print(response.json())
"""out:
{'accessToken': 'eSzVFVWu1Nzi1aZsWMwhd70K2cTN5e',
 'expiresIn': 36000,
 'tokenType': 'Bearer',
 'scope': 'read write',
 'refreshToken': 'nc1Ae8TBaYL2eJyX5iJC1w8nWFMKOQ'}
"""
```
or
```bash
$ curl \
    -H "Content-type: application/json" \
    -X POST -d \
    '{"client_id": "<client_id>", "client_secret": "<client_secret>", "grant_type": "refresh_token", "refresh_token": "<refresh_token>"}' \
    http://localhost:8000/api/auth/token
{"accessToken":"K1x3vWfbBoH8XTYfycUfVJaI7j1ns6","expiresIn":36000,"tokenType":"Bearer","scope":"read write","refreshToken":"r1BXR81vrHD1TX2Hy3UvkSrFysJkU1"}
```

### Revoking token/s

Revoking single token by `http://localhost:8000/api/auth/revoke-token` endpoint:

```python
import requests

response = requests.post("http://localhost:8000/api/auth/revoke-token", json={
    "client_id": "<client_id>", 
    "client_secret": "<client_secret>",
    "token": "<access_token>", 
})
print(response)
"""out:
<Response [204]>
"""
```
or
```bash
$ curl \
    -H "Content-type: application/json" \
    -X POST -d \
    '{"client_id": "<client_id>", "client_secret": "<client_secret>", "token": "<access_token>"}' \
    http://localhost:8000/api/auth/revoke-token
```

## External access token from Google

## Flow

1. Frontend presents login button to user with URL: `http://localhost:8000/api/auth/login/google-oauth2`
2. Backend is redirecting request to Google with proper setup based on `base.py` settings:
    - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY 
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET
    - SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE

    A long with these settings request contains redirect URI to `http://localhost:8000/api/auth/complete/google-oauth2` and random characters to identify state.

    Example URL to where user will be redirected:
    `https://accounts.google.com/o/oauth2/auth?client_id=key&redirect_uri=http://localhost:8000/api/auth/complete/google-oauth2/&state=YkxuVMTmx4Diw1gzD3EgcRuDY6k7id4D&response_type=code&scope=https://www.googleapis.com/auth/userinfo.email+https://www.googleapis.com/auth/userinfo.profile+openid+email+profile`

3. User authorizes `small_eod` application.
4. Google uses `redirect_uri` and make request with authorization code.

    Example callback URI:
    `http://localhost:8000/api/auth/complete/google-oauth2/?code=4/ygHGt7j39aW2i17VRynVIDVILasdasdNfMQa4KCE-XUead4IM0ulU8ffDVlRHHFrtWqgbqWhQCCYv0ORFG7_7BM`

5. Backend receives request with authorization code 
   and exchanges it for Google access and refresh by making another request.

6. #TODO I am not so sure what happens next. How google access token is provided for user :(    


## Authenticating requests

We can authenticate request by placing backend type and external token to authorization header field. Note that you will be authenticating directly with Google:

```python
import requests

response = requests.get("http://localhost:8000/api/cases/", headers={"Authorization": "Bearer google-oauth2 <access_token>"})
print(response, response.json())
"""out:
<Response [200]>
{'count': 0, 'next': None, 'previous': None, 'results': []}
"""
```
or
```bash
$ curl -H "Authorization: Bearer google-oauth2 <access_token>" http://localhost:8000/api/cases/
{'count': 0, 'next': None, 'previous': None, 'results': []}
```

## Converting external token to internal one

I case when we want to covert external google token to internal one, we can use `http://localhost:8000/api/auth/convert-token`:

```python
import requests

response = requests.get("http://localhost:8000/api/auth/convert-token", json={
    "client_id": "<client_id>", 
    "client_secret": "<client_secret>",
    "grant_type": "convert_token", 
    "backend": "google-oauth2", 
    "token": "<google_token>",
})
print(response.json())
"""out:
{'accessToken': '4ASmIHyFZbWGaWiajRPb09VTX2jgBS',
 'expiresIn': 36000,
 'tokenType': 'Bearer',
 'scope': 'read write',
 'refreshToken': 'EbwvibhI7mLv7q3lQnfFRIPNcqLgbh'}
"""
```
or
```bash
$ curl \
    -H "Content-type: application/json" \
    -X POST -d \
    '{"client_id": "<client_id>", "client_secret": "<client_secret>", "grant_type": "convert_token", "backend": "google-oauth2", "token": "<google_token>"}' \
    http://localhost:8000/api/auth/token
{"accessToken":"G0YmYgzOZZqspD9EbXIvmTc7EhqTkP","expiresIn":36000,"tokenType":"Bearer","scope":"read write","refreshToken":"1k4yu9HmBzMXT5nESWYS1BiYvWNfzj"}