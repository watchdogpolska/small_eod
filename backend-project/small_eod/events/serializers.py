from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "case",
            "name",
            "data",
            "comment",
        ]
