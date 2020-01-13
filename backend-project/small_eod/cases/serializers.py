from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Case
from ..tags.models import Tag
from ..dictionaries.models import Feature
from ..generic.serializers import UserLogModelSerializer


class TagField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return [
            self.child.to_representation(item) if item is not None else None
            for item in data.all()
        ]


class CaseSerializer(UserLogModelSerializer):
    tag = TagField()
    feature = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Feature.objects.all()
    )

    class Meta:
        model = Case
        read_only_fields = []
        fields = [
            "id",
            "comment",
            "audited_institution",
            "name",
            "responsible_user",
            "notified_user",
            "feature",
            "tag",
            "created_by",
            "modified_by",
            "created_on",
            "modified_on",
        ]

    def create(self, validated_data):
        tag = [
            Tag.objects.get_or_create(name=tag)[0] for tag in validated_data.pop("tag")
        ]
        audited_institution = validated_data.pop("audited_institution")
        responsible_user = validated_data.pop("responsible_user")
        notified_user = validated_data.pop("notified_user")
        feature = validated_data.pop("feature")
        case = super().create(**validated_data)
        case.tag.set(tag)
        case.audited_institution.set(audited_institution)
        case.responsible_user.set(responsible_user)
        case.notified_user.set(notified_user)
        case.feature.set(feature)
        return case

    def validate_feature(self, value):
        """
        Check that features match minimum & maximum of dictionaries
        """
        for dictionary, items in groupby(
            sorted(value, key=attrgetter("dictionary_id")), attrgetter("dictionary")
        ):
            length = len(list(items))
            if length < dictionary.min_items:
                raise serializers.ValidationError(
                    "Minimum number of items for {} is {}".format(
                        dictionary, dictionary.min_items
                    )
                )
            if length > dictionary.max_items:
                raise serializers.ValidationError(
                    "Maximum number of items for {} is {}".format(
                        dictionary, dictionary.max_items
                    )
                )
        return value


class CaseCountSerializer(CaseSerializer):
    letter_count = serializers.IntegerField(read_only=True)
    note_count = serializers.IntegerField(read_only=True)
    event_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = CaseSerializer.Meta.model
        read_only_fields = CaseSerializer.Meta.read_only_fields
        fields = CaseSerializer.Meta.fields + [
            "letter_count",
            "note_count",
            "event_count",
        ]
