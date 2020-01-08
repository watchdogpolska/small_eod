from .models import AddressData, ExternalIdentifier, JednostkaAdministracyjna, Institution
from rest_framework import serializers


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


class InstitutionSerializer(serializers.ModelSerializer):

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

        new_external_id = ExternalIdentifier.objects.create(**validated_data.pop('external_identifier'))
        new_address = AddressData.objects.create(**validated_data.pop('address'))
        new_admin_unit = JednostkaAdministracyjna.objects.create(**validated_data.pop('administrativeUnit'))

        new_institution = Institution.objects.create(
            external_identifier=new_external_id,
            administrativeUnit=new_admin_unit,
            address=new_address,
            createdBy=self.context['request'].user,
            modifiedBy=self.context['request'].user,
            **validated_data)

        return new_institution
