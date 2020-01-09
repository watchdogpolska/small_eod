from .models import AddressData, ExternalIdentifier, JednostkaAdministracyjna, Institution
from rest_framework import serializers

from ..generic.serializers import UserLogModelSerializer


class AdministrativeUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = JednostkaAdministracyjna
        exclude = ['id', ]


class AddressDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressData
        fields = '__all__'
        read_only_fields = ['id', ]


class ExternalIdentifierSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExternalIdentifier
        exclude = ['id', ]


class InstitutionSerializer(UserLogModelSerializer):

    address = AddressDataSerializer()
    external_identifier = ExternalIdentifierSerializer()
    administrativeUnit = AdministrativeUnitSerializer()

    class Meta:
        model = Institution
        read_only_fields = ['createdBy', 'modifiedBy', 'createdOn', 'modifiedOn', 'id']
        fields = [
            'modifiedOn',
            'name',
            'external_identifier',
            'createdOn',
            'administrativeUnit',
            'address',
            'modifiedBy',
            'createdBy',
            'id',
        ]

    def create(self, validated_data):

        validated_data['external_identifier'] = ExternalIdentifier.objects.create(
            **validated_data.pop('external_identifier')
        )
        validated_data['address'] = AddressData.objects.create(
            **validated_data.pop('address')
        )
        validated_data['administrativeUnit'] = JednostkaAdministracyjna.objects.create(
            **validated_data.pop('administrativeUnit')
        )

        return super().create(validated_data)
