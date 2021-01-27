from django.utils import timezone
from rest_framework import serializers
from rest_framework.fields import CharField

from ..generic.serializers import UserLogModelSerializer
from .fields import DurationField
from .models import Collection
from .signer import JWTSigner

MINUTE = 60

signer = JWTSigner()


class CollectionSerializer(UserLogModelSerializer):
    class Meta:
        model = Collection
        fields = ["id", "name", "comment", "public", "expired_on", "query"]


class TokenSetSerializer(serializers.Serializer):
    lifetime = DurationField(min_value=60, default=None)
    access_token = CharField(read_only=True)

    def create(self, validated_data):
        lifetime = (
            timezone.timedelta(seconds=validated_data["lifetime"])
            if self.validated_data["lifetime"]
            else None
        )
        user = self.context["request"].user
        token = signer.sign(
            subject=f"collection-{self.context['collection'].pk}",
            request=self.context["request"],
            lifetime=lifetime,
            extra={"user_id": user.pk},
        )

        return {"lifetime": validated_data["lifetime"], "access_token": token}
