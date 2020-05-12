from .models import Feature, FeatureOption
from rest_framework import serializers
from ..generic.serializers import UserLogModelSerializer
from rest_framework.serializers import ModelSerializer


class FeatureOptionSerializer(ModelSerializer):
    features = serializers.PrimaryKeyRelatedField(
        many=False, default=None, queryset=Feature.objects.all()
    )

    class Meta:
        model = FeatureOption
        fields = ["id", "name", "features"]


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
        features = super().create(validated_data)
        for feature_data in features_data:
            FeatureOption.objects.create(features=features, **feature_data)
        return features
