from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.utils import timezone
import jwt


class JWTSigner:
    def get_key(self):
        return settings.SECRET_KEY

    def validate_iss_and_aud(self, iss, aud):
        if not iss:
            raise jwt.exceptions.InvalidAudienceError(
                "Invalid / missing issuer on server-side"
            )
        if not aud:
            raise jwt.exceptions.InvalidAudienceError(
                "Invalid / missing audience on server-side"
            )

    def sign(
        self, subject, request=None, lifetime=None, iss=None, aud=None, extra=None
    ):
        if request:
            site = get_current_site(request)
            iss = iss or site.domain
            aud = aud or site.domain

        self.validate_iss_and_aud(iss, aud)

        claim = {
            "iss": iss,
            "aud": aud,
            "sub": subject,
        }

        if lifetime:
            expire_at = timezone.now() + lifetime
            claim["exp"] = int(expire_at.strftime("%s"))

        claim.update(extra or {})

        return jwt.encode(payload=claim, key=self.get_key(), algorithm="HS512").decode(
            "utf-8"
        )

    def unsign(self, payload, request=None, iss=None, aud=None):
        if request:
            site = get_current_site(request)
            iss = iss or site.domain
            aud = aud or site.domain

        self.validate_iss_and_aud(iss, aud)

        return jwt.decode(
            jwt=payload,
            key=self.get_key(),
            audience=aud,
            issuer=iss,
            algorithms=["HS512"],
        )
