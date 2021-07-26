from uuid import uuid4

from django.conf import settings
from rest_framework import serializers

from ..cases.models import Case
from ..channels.models import Channel
from ..files.apps import minio_app
from ..files.serializers import FileSerializer
from ..generic.serializers import UserLogModelSerializer
from ..institutions.models import Institution
from .models import DocumentType, Letter, ReferenceNumber


class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = ["id", "name"]


class ReferenceNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceNumber
        fields = ["id", "name"]


class LetterSerializer(UserLogModelSerializer):
    reference_number = serializers.CharField(default=None)
    document_type = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=DocumentType.objects.all()
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
            "direction",
            "channel",
            "final",
            "date",
            "reference_number",
            "institution",
            "case",
            "attachments",
            "comment",
            "document_type",
            "created_on",
            "created_by",
            "modified_on",
            "modified_by",
        ]

    def create(self, validated_data):
        # Reference numbers use the "tag" mode - they're provided by value and
        # created if not matching any known objects.
        reference_number_value = validated_data.pop("reference_number")
        reference_number = (
            ReferenceNumber.objects.get_or_create(name=reference_number_value)[0]
            if reference_number_value is not None
            else None
        )

        channel = validated_data.pop("channel")
        document_type = validated_data.pop("document_type")
        institution = validated_data.pop("institution")
        case = validated_data.pop("case")

        letter = super().create(validated_data)
        letter.channel = channel
        letter.document_type = document_type
        letter.reference_number = reference_number
        letter.institution = institution
        letter.case = case
        letter.save()
        return letter

    def update(self, instance, validated_data):
        """
        nested - variable storing representations of the nested objects
        of LetterSerializer (Channel, Address and DocumentType).
        Iterating over those 3 and updating fields of the related objects,
        using key-value pairs from PATCH request.
        """
        # NOTE(rwa_kulszowa): the section below doesn't seem to do much.
        nested = []
        for nested_object in nested:
            for attr, value in nested_object["data"].items():
                setattr(nested_object["instance"], attr, value)
            nested_object["instance"].save()

        # Create a new reference number if necessary.
        # See comment in `create`.
        if "reference_number" in validated_data:
            reference_number_value = validated_data.pop("reference_number")
            reference_number = (
                ReferenceNumber.objects.get_or_create(name=reference_number_value)[0]
                if reference_number_value is not None
                else None
            )
            validated_data["reference_number"] = reference_number

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
