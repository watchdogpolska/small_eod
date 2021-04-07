from rest_framework.serializers import SlugRelatedField

from ..generic.serializers import UserLogModelSerializer
from .models import Note


class NoteSerializer(UserLogModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "case", "comment"]
