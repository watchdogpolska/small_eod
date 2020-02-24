from uuid import uuid4
from django.conf import settings
from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer
from ..cases.models import Case
from ..institutions.models import Institution, AddressData
from ..institutions.serializers import AddressDataNestedSerializer
from ..channels.models import Channel
from ..channels.serializers import ChannelNestedSerializer
from ..files.apps import minio_app
from ..files.serializers import FileSerializer


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["name", "id"]


class LetterSerializer(UserLogModelSerializer):
    description = DescriptionSerializer()
    case = serializers.PrimaryKeyRelatedField(many=False, queryset=Case.objects.all())
    institution = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Institution.objects.all()
    )
    address = AddressDataNestedSerializer()
    channel = ChannelNestedSerializer()
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
            "description",
            "created_on",
            "created_by",
            "modified_on",
            "modified_by",
        ]

    def create(self, validated_data):
        validated_data["address"] = AddressData.objects.create(
            **validated_data.pop("address")
        )
        validated_data["channel"] = Channel.objects.create(
            **validated_data.pop("channel")
        )
        validated_data["description"] = Description.objects.create(
            **validated_data.pop("description")
        )
        institution = validated_data.pop("institution")
        case = validated_data.pop("case")

        letter = super().create(validated_data)

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
        nested = [
            {"instance": instance.address, "data": validated_data.pop("address", {})},
            {"instance": instance.channel, "data": validated_data.pop("channel", {})},
            {
                "instance": instance.description,
                "data": validated_data.pop("description", {}),
            },
        ]
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
