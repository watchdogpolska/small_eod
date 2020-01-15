from .models import Dictionary, Feature
from ..generic.serializers import UserLogModelSerializer


class NestedFeatureSerializer(UserLogModelSerializer):
    class Meta:
        model = Feature
        fields = ["id", "name"]


class DictionarySerializer(UserLogModelSerializer):
    values = NestedFeatureSerializer(many=True)

    class Meta:
        model = Dictionary
        fields = ["name", "active", "min_items", "max_items", "values"]

    def create(self, validated_data):
        features_data = validated_data.pop("values")
        dictionary = super().create(validated_data)
        for feature_data in features_data:
            Feature.objects.create(dictionary=dictionary, **feature_data)
        return dictionary
