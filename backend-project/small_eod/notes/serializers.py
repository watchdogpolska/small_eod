from rest_framework import serializers
from itertools import groupby
from operator import attrgetter
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["case", "comment"]
