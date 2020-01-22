from uuid import uuid4
from urllib.parse import urljoin

from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer
from ..files.apps import minio_app

from small_eod.files.serializers import FileSerializer


class LetterSerializer(UserLogModelSerializer):
    attachment = FileSerializer(many=True, read_only=True)

    class Meta:
        model = Letter
        fields = [
            "id",
            "name",
            "direction",
            "channel",
            "final",
            "date",
            "identifier",
            "institution",
            "address",
            "case",
            "attachment",
            "ordering",
            "comment",
            "excerpt",
            "created_on",
            "created_by",
            "modified_on",
            "modified_by",
        ]


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = [
            "name",
        ]


class SignRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    method = serializers.CharField(read_only=True)
    url = serializers.CharField(read_only=True)
    formData = serializers.CharField(read_only=True)
    path = serializers.CharField(read_only=True)

    def create(self, **validated_data):
        path = f'{uuid4()}/{validated_data["name"]}'
        url, form_data = minio_app.presigned_post_form_data("files", path)
        path = urljoin(url, path)
        return {
            "name": validated_data["name"],
            "method": "POST",
            "url": url,
            "formData": form_data,
            "path": path,
        }
