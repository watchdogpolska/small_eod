from rest_framework import serializers
from .models import File
from ..files.apps import minio_app
from django.conf import settings
from django.utils import timezone


class FileSerializer(serializers.ModelSerializer):
    letter = serializers.PrimaryKeyRelatedField(read_only=True)
    download_url = serializers.SerializerMethodField(read_only=True)

    def get_download_url(self, obj):
        return minio_app.presigned_get_object(
            settings.MINIO_BUCKET, obj.path, expires=timezone.timedelta(hours=3)
        )

    class Meta:
        model = File
        fields = ["id", "path", "download_url", "name", "letter"]
        read_only_fields = []
