from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer


class LetterSerializer(UserLogModelSerializer):
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
