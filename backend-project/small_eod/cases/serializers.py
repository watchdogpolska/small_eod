from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Case
from ..tags.models import Tag
from ..features.models import FeatureOption
from ..generic.serializers import UserLogModelSerializer
from ..users.models import User
from ..tags.fields import TagField


class CurrentUserListDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return [serializer_field.context["request"].user]


class CaseSerializer(UserLogModelSerializer):
    tags = TagField()
    featureoptions = serializers.PrimaryKeyRelatedField(
        many=True, default=[], queryset=FeatureOption.objects.all()
    )
    responsible_users = serializers.PrimaryKeyRelatedField(
        many=True, default=CurrentUserListDefault(), queryset=User.objects.all()
    )
    notified_users = serializers.PrimaryKeyRelatedField(
        many=True, default=CurrentUserListDefault(), queryset=User.objects.all()
    )

    class Meta:
        model = Case
        read_only_fields = []
        fields = [
            "id",
            "comments",
            "audited_institutions",
            "name",
            "responsible_users",
            "notified_users",
            "featureoptions",
            "tags",
            "created_by",
            "modified_by",
            "created_on",
            "modified_on",
        ]
        extra_kwargs = {"audited_institutions": {"default": []}}

    def create(self, validated_data):
        tag = [
            Tag.objects.get_or_create(name=tag)[0] for tag in validated_data.pop("tags")
        ]
        audited_institutions = validated_data.pop("audited_institutions")
        responsible_users = validated_data.pop("responsible_users")
        notified_users = validated_data.pop("notified_users")
        featureoptions = validated_data.pop("featureoptions")
        case = super().create(validated_data)
        case.tags.set(tag)
        case.audited_institutions.set(audited_institutions)
        case.responsible_users.set(responsible_users)
        case.notified_users.set(notified_users)
        case.featureoptions.set(featureoptions)
        return case

    def validate_featureoptions(self, value):
        """
        Check that featureoptions match minimum & maximum of options
        """
        for feature, items in groupby(
            sorted(value, key=attrgetter("features_id")), attrgetter("features")
        ):
            length = len(list(items))
            if length < feature.min_options:
                raise serializers.ValidationError(
                    "Minimum number of items for {} is {}".format(
                        feature, feature.min_options
                    )
                )
            if length > feature.max_options:
                raise serializers.ValidationError(
                    "Maximum number of items for {} is {}".format(
                        feature, feature.max_options
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
        extra_kwargs = CaseSerializer.Meta.extra_kwargs
