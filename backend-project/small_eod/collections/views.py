from rest_framework import viewsets

from .models import Collection
from .serializers import CollectionSerializer
from ..cases.serializers import CaseSerializer
from ..cases.models import Case
from ..notes.serializers import NoteSerializer
from ..notes.models import Note
from ..events.serializers import EventSerializer
from ..events.models import Event
from ..letters.serializers import LetterSerializer
from ..letters.models import Letter


def parse_query(query):
    # TODO: Add extensive query parser
    return {"pk__in": [int(x) for x in query.split(",")]}


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CaseSerializer

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        return Case.objects.filter(**parse_query(collection.query)).with_counter().all()


class BaseSubCollection(viewsets.ReadOnlyModelViewSet):
    model = None

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        case = Case.objects.filter(**parse_query(collection.query)).get(
            pk=self.kwargs["case_pk"]
        )
        return self.model.objects.filter(case=case).all()


class EventViewSet(BaseSubCollection):
    serializer_class = EventSerializer
    model = Event


class NoteViewSet(BaseSubCollection):
    serializer_class = NoteSerializer
    model = Note


class LetterViewSet(BaseSubCollection):
    serializer_class = LetterSerializer
    model = Letter
