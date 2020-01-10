from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "id",
            "name",
            "city",
            "voivodeship",
            "flat_no",
            "street",
            "postal_code",
            "house_no",
            "email",
            "epuap",
        ]
