from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Letter, Description


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = [
            "case",
            "direction",
            "name",
            "channel",
            "final",
            "date",
            "identifier",
            "institution",
            "address",
            "ordering",
            "comment",
            "excerpt",
        ]


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            "name",
        ]
