from .models import Event
from ..generic.serializers import UserLogModelSerializer


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
