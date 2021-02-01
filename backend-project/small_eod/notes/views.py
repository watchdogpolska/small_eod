from rest_framework import viewsets

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Note
from .serializers import NoteSerializer
from .filterset import NoteFilterSet


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = NoteFilterSet
    ordering_fields = [
        "id",
        "case__name",
    ]
