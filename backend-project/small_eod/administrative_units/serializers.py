from rest_framework import serializers

from .models import AdministrativeUnit


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=False, default=None, slug_field="name", read_only=True
    )

    class Meta:
        model = AdministrativeUnit
        fields = ["id", "parent", "name", "category", "slug", "updated_on", "active"]
