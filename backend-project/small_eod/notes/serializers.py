from .models import Note
from ..generic.serializers import UserLogModelSerializer


class NoteSerializer(UserLogModelSerializer):
    class Meta:
        model = Note
        fields = ["case", "comment"]
