from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "id",
            "path",
            "name",
        ]


class FileRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = [
            "id",
            "path",
            "name",
            "letter",
        ]
