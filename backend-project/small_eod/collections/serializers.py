from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Collection
from ..generic.serializers import UserLogModelSerializer


class CollectionSerializer(UserLogModelSerializer):
    class Meta:
        model = Collection
        fields = [
            "id",
            "comment",
            "public",
            "expired_on",
            "query",
        ]
