from uuid import uuid4
from django.conf import settings
from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer
from ..cases.models import Case
from ..institutions.models import Institution
from ..channels.models import Channel
from ..files.apps import minio_app
from ..files.serializers import FileSerializer


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["name"]


class LetterSerializer(UserLogModelSerializer):
    description = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Description.objects.all()
    )
    case = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Case.objects.all()
    )
    institution = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Institution.objects.all()
    )
    channel = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Channel.objects.all()
    )
    attachments = FileSerializer(many=True, read_only=True)

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
            "case",
            "attachments",
            "ordering",
            "comment",
            "excerpt",
            "description",
            "created_on",
            "created_by",
            "modified_on",
            "modified_by",
        ]

    def create(self, validated_data):
        channel = validated_data.pop("channel")
        description = validated_data.pop("description")
        institution = validated_data.pop("institution")
        case = validated_data.pop("case")

        letter = super().create(validated_data)
        letter.channel = channel
        letter.description = description
        letter.institution = institution
        letter.case = case
        letter.save()
        return letter

    def update(self, instance, validated_data):
        """
        nested - variable storing representations of the nested objects
        of LetterSerializer (Channel, Address and Description).
        Iterating over those 3 and updating fields of the related objects,
        using key-value pairs from PATCH request.
        """
        nested = []
        for nested_object in nested:
            for attr, value in nested_object["data"].items():
                setattr(nested_object["instance"], attr, value)
            nested_object["instance"].save()
        return super().update(instance, validated_data)


class SignRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    method = serializers.CharField(read_only=True)
    url = serializers.CharField(read_only=True)
    formData = serializers.DictField(read_only=True, child=serializers.CharField())
    path = serializers.CharField(read_only=True)

    def create(self, validated_data):
        path = f'{uuid4()}/{validated_data["name"]}'
        url, form_data = minio_app.presigned_post_form_data(settings.MINIO_BUCKET, path)
        return {
            "name": validated_data["name"],
            "method": "POST",
            "url": url,
            "formData": form_data,
            "path": path,
        }
