from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ..administrative_units.models import AdministrativeUnit
from ..cases.models import Case, Tag
from ..channels.models import Channel
from ..events.models import Event
from ..features.models import Feature, FeatureOption
from ..institutions.models import Institution
from ..letters.models import DocumentType, Letter
from ..notes.models import Note
from ..tags.models import Tag
from ..users.models import User
from .filterset import (
    AdministrativeUnitAutocompleteFilterSet,
    CaseAutocompleteFilterSet,
    ChannelAutocompleteFilterSet,
    DocumentTypeAutocompleteFilterSet,
    EventAutocompleteFilterSet,
    FeatureAutocompleteFilterSet,
    FeatureOptionAutocompleteFilterSet,
    InstitutionAutocompleteFilterSet,
    LetterAutocompleteFilterSet,
    NoteAutocompleteFilterSet,
    TagAutocompleteFilterSet,
    UserAutocompleteFilterSet,
)
from .serializers import (
    AdministrativeUnitAutocompleteSerializer,
    CaseAutocompleteSerializer,
    ChannelAutocompleteSerializer,
    DocumentTypeAutocompleteSerializer,
    EventAutocompleteSerializer,
    FeatureAutocompleteSerializer,
    FeatureOptionAutocompleteSerializer,
    InstitutionAutocompleteSerializer,
    LetterAutocompleteSerializer,
    NoteAutocompleteSerializer,
    TagAutocompleteSerializer,
    UserAutocompleteSerializer,
)


class AdministrativeUnitAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdministrativeUnit.objects.only("id", "name").all()
    serializer_class = AdministrativeUnitAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdministrativeUnitAutocompleteFilterSet


class CaseAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.only("id", "name").all()
    serializer_class = CaseAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CaseAutocompleteFilterSet


class ChannelAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.only("id", "name").all()
    serializer_class = ChannelAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChannelAutocompleteFilterSet


class DocumentTypeAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentType.objects.only("id", "name").all()
    serializer_class = DocumentTypeAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DocumentTypeAutocompleteFilterSet


class EventAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.only("id", "name").all()
    serializer_class = EventAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventAutocompleteFilterSet


class FeatureAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feature.objects.only("id", "name").all()
    serializer_class = FeatureAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureAutocompleteFilterSet


class FeatureOptionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeatureOption.objects.only("id", "name").all()
    serializer_class = FeatureOptionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureOptionAutocompleteFilterSet


class InstitutionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.only("id", "name").all()
    serializer_class = InstitutionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstitutionAutocompleteFilterSet


class LetterAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Letter.objects.only("id", "name").all()
    serializer_class = LetterAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LetterAutocompleteFilterSet


class NoteAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Note.objects.only("id", "name").all()
    serializer_class = NoteAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NoteAutocompleteFilterSet


class TagAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.only("id", "name").all()
    serializer_class = TagAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagAutocompleteFilterSet


class UserAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.only("id", "username").all()
    serializer_class = UserAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserAutocompleteFilterSet
