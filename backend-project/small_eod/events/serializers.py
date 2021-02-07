from ..generic.serializers import UserLogModelSerializer
from .models import Event


class EventSerializer(UserLogModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "case",
            "name",
            "date",
            "comment",
        ]
