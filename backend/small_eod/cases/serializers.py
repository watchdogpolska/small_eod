from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Case
from ..tags.models import Tag
from ..dictionaries.models import Feature

class CaseSerializer(serializers.ModelSerializer):
    tag = serializers.ListField()
    feature = serializers.PrimaryKeyRelatedField(many=True, queryset=Feature.objects.all())

    createdBy = serializers.PrimaryKeyRelatedField(read_only=True)
    modifiedBy = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Case
        read_only_fields = ['createdOn', 'modifiedOn']
        fields = ['id', "comment", "auditedInstitution","name", "responsibleUser", "notifiedUser", "feature", "tag", "createdBy", "modifiedBy", "createdOn", "modifiedOn"]

    def create(self, validated_data):
        tag = [Tag.objects.get_or_create(name=tag)[0] for tag in validated_data.pop('tag')]
        auditedInstitution = validated_data.pop('auditedInstitution')
        responsibleUser = validated_data.pop('responsibleUser')
        notifiedUser = validated_data.pop('notifiedUser')
        feature = validated_data.pop('feature')
        case = Case.objects.create(**validated_data)
        case.tag.set(tag)
        case.auditedInstitution.set(auditedInstitution)
        case.responsibleUser.set(responsibleUser)
        case.notifiedUser.set(notifiedUser)
        case.feature.set(feature)
        return case

    def validate_feature(self, value):
        """
        Check that features match minimum & maximum of dictionaries
        """
        for dictionary, items in groupby(sorted(value, key=attrgetter("dictionary_id")), attrgetter("dictionary")):
            length = len(list(items));
            import pdb; pdb.set_trace();
            if length < dictionary.minItems:
                raise serializers.ValidationError("Minimum number of items for {} is {}".format(dictionary, dictionary.minItems))
            if length > dictionary.maxItems:
                raise serializers.ValidationError("Maximum number of items for {} is {}".format(dictionary, dictionary.minItems))
        return value