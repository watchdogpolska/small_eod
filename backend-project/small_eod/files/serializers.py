from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "letter",
            "path",
            "name",
        ]
