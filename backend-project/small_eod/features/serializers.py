from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from ..generic.serializers import UserLogModelSerializer
from .models import Feature, FeatureOption


class FeatureOptionSerializer(ModelSerializer):
    feature = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Feature.objects.all()
    )

    class Meta:
        model = FeatureOption
        fields = ["id", "name", "feature"]


class NestedFeatureOptionSerializer(ModelSerializer):
    class Meta:
        model = FeatureOptionSerializer.Meta.model
        fields = ["id", "name"]


class FeatureSerializer(UserLogModelSerializer):
    featureoptions = NestedFeatureOptionSerializer(many=True, default=[])

    class Meta:
        model = Feature
        fields = ["id", "name", "min_options", "max_options", "featureoptions"]

    def create(self, validated_data):
        features_data = validated_data.pop("featureoptions")
        feature = super().create(validated_data)
        for feature_data in features_data:
            FeatureOption.objects.create(feature=feature, **feature_data)
        return feature
