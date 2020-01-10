from rest_framework import serializers

from .models import Dictionary, Feature


class NestedFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "name"]


class DictionarySerializer(serializers.ModelSerializer):
    values = NestedFeatureSerializer(many=True)

    class Meta:
        model = Dictionary
        fields = ["name", "active", "min_items", "max_items", "values"]

    def create(self, validated_data):
        features_data = validated_data.pop("values")
        dictionary = Dictionary.objects.create(**validated_data)
        for feature_data in features_data:
            Feature.objects.create(dictionary=dictionary, **feature_data)
        return dictionary
