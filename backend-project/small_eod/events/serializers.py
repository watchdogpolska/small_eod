from rest_framework.serializers import SlugRelatedField

from ..generic.serializers import UserLogModelSerializer
from .models import Event


class EventListSerializer(UserLogModelSerializer):
    case = SlugRelatedField(many=False, default=None, slug_field="name", read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "case",
            "name",
            "date",
            "comment",
        ]


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
