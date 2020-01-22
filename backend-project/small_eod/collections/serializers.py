from .models import Collection
from ..generic.serializers import UserLogModelSerializer


class CollectionSerializer(UserLogModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "comment",
            "public",
            "expired_on",
            "query",
        ]
