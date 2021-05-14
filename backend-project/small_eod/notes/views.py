from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from ..notifications.views import SendNotificationsMixin
from .filterset import NoteFilterSet
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet, SendNotificationsMixin):
    notified_users = "case.notified_users"
    ignored_fields = ["modified_by"]
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = NoteFilterSet
    ordering_fields = [
        "id",
        "case__name",
    ]
