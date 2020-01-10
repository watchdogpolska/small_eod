from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "name",
        ]
