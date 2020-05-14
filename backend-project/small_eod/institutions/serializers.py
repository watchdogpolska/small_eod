from .models import (
    AddressData,
    ExternalIdentifier,
    JednostkaAdministracyjna,
    Institution,
)
from rest_framework import serializers
from ..generic.serializers import UserLogModelSerializer


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
        many=False, queryset=JednostkaAdministracyjna.objects.all(),
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

    def validate_administrative_unit(self, admin):
        admin_unit = JednostkaAdministracyjna.objects.get(pk=admin.id)
        if admin_unit.category.level != 3:
            raise serializers.ValidationError(
                "Administrative unit should be of level 3 (community)"
            )
        return admin

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

    def update(self, instance, validated_data):
        """
        institution_nested - variable storing representations of the nested objects
        of InstitutionSerializer (External Identifier and Address).
        Iterating over those 2 and updating fields of the related objects,
        using key-value pairs from PATCH request.
        """
        institution_nested = [
            {
                "instance": instance.external_identifier,
                "data": validated_data.pop("external_identifier", {}),
            },
            {"instance": instance.address, "data": validated_data.pop("address", {})},
        ]

        for nested_object in institution_nested:
            for attr, value in nested_object["data"].items():
                setattr(nested_object["instance"], attr, value)
            nested_object["instance"].save()
        return super().update(instance, validated_data)
