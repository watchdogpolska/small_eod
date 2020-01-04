from rest_framework import serializers

from dictionary.models import Dictionary
from case.models import Case

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = '__all__'
