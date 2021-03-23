from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from ..cases.models import Case
from .filterset import NoteFilterSet
from .models import Note
from .serializers import NoteListSerializer, NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = NoteFilterSet
    ordering_fields = [
        "id",
        "case__name",
    ]

    def get_queryset(self):
        if self.action == "list":
            return Note.objects.prefetch_related(
                Prefetch("case", queryset=Case.objects.all().only("name"))
            )
        return super().get_queryset()

    def get_serializer_class(self):
        if self.action == "list":
            return NoteListSerializer
        return super().get_serializer_class()
