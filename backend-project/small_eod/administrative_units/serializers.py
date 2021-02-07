from rest_framework import serializers

from .models import AdministrativeUnit


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeUnit
        fields = ["id", "parent", "name", "category", "slug", "updated_on", "active"]
