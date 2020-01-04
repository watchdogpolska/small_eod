from rest_framework import serializers

from .models import Dictionary


class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
