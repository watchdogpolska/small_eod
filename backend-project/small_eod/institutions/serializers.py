from .models import (
    JednostkaAdministracyjna,
    Institution,
)
from rest_framework import serializers
from ..generic.serializers import UserLogModelSerializer
from ..tags.serializers import TagSerializer


class InstitutionSerializer(UserLogModelSerializer):
    administrative_unit = serializers.PrimaryKeyRelatedField(
        many=False, queryset=JednostkaAdministracyjna.objects.all(),
    )

    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Institution
        fields = [
            "id",
            "modified_by",
            "created_by",
            "modified_on",
            "created_on",
            "name",
            "administrative_unit",
            "email",
            "city",
            "epuap",
            "street",
            "house_no",
            "postal_code",
            "flat_no",
            "nip",
            "regon",
            "comment",
            "tags",
        ]

    def validate_administrative_unit(self, admin):
        admin_unit = JednostkaAdministracyjna.objects.get(pk=admin.id)
        if admin_unit.category.level != 3:
            raise serializers.ValidationError(
                "Administrative unit should be of level 3 (community)"
            )
        return admin

    def create(self, validated_data):
        administrative_unit = validated_data.pop("administrative_unit")
        institution = super().create(validated_data)
        institution.administrative_unit = administrative_unit
        institution.save()
        return institution
