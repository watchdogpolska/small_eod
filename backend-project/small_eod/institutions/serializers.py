from .models import (
    JednostkaAdministracyjna,
    Institution,
)
from ..tags.models import Tag
from rest_framework import serializers
from ..generic.serializers import UserLogModelSerializer
<<<<<<< HEAD
<<<<<<< HEAD
from ..tags.fields import TagField
=======
from ..tags.serializers import TagSerializer
>>>>>>> 7be475e... Add tests according to the issue
=======
from ..tags.fields import TagField
>>>>>>> 6eb55e9... Add serializer tests


class InstitutionSerializer(UserLogModelSerializer):
    administrative_unit = serializers.PrimaryKeyRelatedField(
        many=False, queryset=JednostkaAdministracyjna.objects.all(),
    )

<<<<<<< HEAD
<<<<<<< HEAD
    tags = TagField()
=======
    tags = TagSerializer(read_only=True, many=True)
>>>>>>> 7be475e... Add tests according to the issue
=======
    tags = TagField()
>>>>>>> 6eb55e9... Add serializer tests

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
        tag = [
            Tag.objects.get_or_create(name=tag)[0] for tag in validated_data.pop("tags")
        ]
        administrative_unit = validated_data.pop("administrative_unit")
        institution = super().create(validated_data)
        institution.tags.set(tag)
        institution.administrative_unit = administrative_unit
        institution.save()
        return institution

    def update(self, instance, validated_data):
        tags = (
            [
                Tag.objects.get_or_create(name=tag)[0]
                for tag in validated_data.pop("tags")
            ]
            if "tags" in validated_data
            else None
        )
        institution = super().update(instance, validated_data)
        if tags:
            institution.tags.set(tags)
        return institution
