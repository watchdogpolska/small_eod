header_prefix = "Bearer "


def get_token(request):
    auth = request.META.get("HTTP_AUTHORIZATION")
    if auth and auth.startswith(header_prefix):
        return auth[len(header_prefix) :]
    return request.GET.get("token", None)
