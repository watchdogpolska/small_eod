from rest_framework import serializers
from .models import Letter, Description
from ..generic.serializers import UserLogModelSerializer
from ..cases.models import Case
from ..institutions.models import Institution
from ..institutions.serializers import AddressDataNestedSerializer
from ..channels.serializers import ChannelNestedSerializer


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = ["name", "letter"]


class LetterSerializer(UserLogModelSerializer):
    description = serializers.ListField()
    case = serializers.PrimaryKeyRelatedField(many=False, queryset=Case.objects.all())
    institution = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Institution.objects.all()
    )
    address = AddressDataNestedSerializer()
    channel = ChannelNestedSerializer()

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
            "description",
        ]

    def create(self, validated_data):
        descriptions = validated_data.pop("description")

        validated_data["address"] = Description.objects.create(
            **validated_data.pop("address")
        )
        validated_data["channel"] = Description.objects.create(
            **validated_data.pop("channel")
        )
        validated_data["description"] = Description.objects.create(
            **validated_data.pop("description")
        )
        institution = validated_data.pop("institution")
        case = validated_data.pop("case")

        letter = super().create(validated_data)

        for description in descriptions:
            Description.objects.get_or_create(name=description, letter=letter)

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
