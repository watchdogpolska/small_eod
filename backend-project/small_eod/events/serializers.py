from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Event
from ..generic.serializers import UserLogModelSerializer


class EventSerializer(UserLogModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "case",
            "name",
            "data",
            "comment",
        ]
