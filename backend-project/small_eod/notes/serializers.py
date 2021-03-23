from rest_framework.serializers import SlugRelatedField
from ..generic.serializers import UserLogModelSerializer
from .models import Note


class NoteListSerializer(UserLogModelSerializer):
    case = SlugRelatedField(many=False, default=None, slug_field="name", read_only=True)

    class Meta:
        model = Note
        fields = ["id", "case", "comment"]


class NoteSerializer(UserLogModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "case", "comment"]
