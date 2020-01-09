from rest_framework import serializers

from .models import Case
from ..tags.models import Tag


class CaseSerializer(serializers.ModelSerializer):
    tag = serializers.ListField()
    dictionary = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Case
        read_only_fields = ['createdBy', 'modifiedBy', 'createdOn', 'modifiedOn', 'id']
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        tags = validated_data.pop('tag')
        new_case = Case.objects.create(**validated_data)
        for tag in tags:
            Tag.objects.create(tag_field=tag, case=new_case)

        return new_case
