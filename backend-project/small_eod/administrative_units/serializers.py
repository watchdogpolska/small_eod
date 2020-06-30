from .models import AdministrativeUnit
from rest_framework import serializers


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeUnit
        fields = ["id", "parent", "name", "category", "slug", "updated_on", "active"]
