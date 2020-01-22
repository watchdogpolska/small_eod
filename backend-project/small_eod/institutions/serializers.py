from .models import (
    AddressData,
    ExternalIdentifier,
    JednostkaAdministracyjna,
    Institution,
)
from rest_framework import serializers

from ..generic.serializers import UserLogModelSerializer


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = JednostkaAdministracyjna
        fields = ["id", "parent", "name", "category", "slug", "updated_on", "active"]


class AddressDataNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddressData
        fields = [
            "email",
            "city",
            "epuap",
            "street",
            "house_no",
            "postal_code",
            "flat_no",
        ]


class ExternalIdentifierNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalIdentifier
        fields = ["nip", "regon"]


class InstitutionSerializer(UserLogModelSerializer):

    address = AddressDataNestedSerializer()
    external_identifier = ExternalIdentifierNestedSerializer()
    administrative_unit = serializers.PrimaryKeyRelatedField(
        many=False, queryset=JednostkaAdministracyjna.objects.all()
    )

    class Meta:
        model = Institution
        fields = [
            "id",
            "modified_by",
            "created_by",
            "modified_on",
            "created_on",
            "name",
            "external_identifier",
            "administrative_unit",
            "address",
        ]

    def create(self, validated_data):

        validated_data["external_identifier"] = ExternalIdentifier.objects.create(
            **validated_data.pop("external_identifier")
        )
        validated_data["address"] = AddressData.objects.create(
            **validated_data.pop("address")
        )
        administrative_unit = validated_data.pop("administrative_unit")
        institution = super().create(validated_data)
        institution.administrative_unit = administrative_unit
        institution.save()
        return institution
