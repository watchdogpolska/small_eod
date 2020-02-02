from .models import (
    AddressData,
    ExternalIdentifier,
    JednostkaAdministracyjna,
    Institution,
)
from django.db import models
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
        many=False,
        queryset=JednostkaAdministracyjna.objects.filter(
            models.Q(category__level=3)
        ).all(),
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

    def update(self, instance, validated_data):
        institution_nested = [
            {
                "instance": instance.external_identifier,
                "data": validated_data.pop("external_identifier"),
            },
            {"instance": instance.address, "data": validated_data.pop("address")},
        ]

        for nested_object in institution_nested:
            for attr, value in nested_object["data"].items():
                setattr(nested_object["instance"], attr, value)
            nested_object["instance"].save()
        return super().update(instance, validated_data)
