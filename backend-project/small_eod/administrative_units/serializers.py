from .models import JednostkaAdministracyjna
from rest_framework import serializers


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = JednostkaAdministracyjna
        fields = ["id", "parent", "name", "category", "slug", "updated_on", "active"]
