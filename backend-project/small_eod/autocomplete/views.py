from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ..administrative_units.filterset import AdministrativeUnitFilterSet
from ..administrative_units.models import AdministrativeUnit
from ..cases.filterset import CaseFilterSet
from ..cases.models import Case
from ..channels.filterset import ChannelFilterSet
from ..channels.models import Channel
from ..events.filterset import EventFilterSet
from ..events.models import Event
from ..features.filterset import FeatureFilterSet, FeatureOptionFilterSet
from ..features.models import Feature, FeatureOption
from ..institutions.filterset import InstitutionFilterSet
from ..institutions.models import Institution
from ..letters.filterset import DocumentTypeFilterSet
from ..letters.models import DocumentType
from ..tags.filterset import TagFilterSet
from ..tags.models import Tag
from ..users.filterset import UserFilterSet
from ..users.models import User
from .serializers import (
    AdministrativeUnitAutocompleteSerializer,
    CaseAutocompleteSerializer,
    ChannelAutocompleteSerializer,
    DocumentTypeAutocompleteSerializer,
    EventAutocompleteSerializer,
    FeatureAutocompleteSerializer,
    FeatureOptionAutocompleteSerializer,
    InstitutionAutocompleteSerializer,
    TagAutocompleteSerializer,
    UserAutocompleteSerializer,
)


class AdministrativeUnitAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdministrativeUnit.objects.only("id", "name").all()
    serializer_class = AdministrativeUnitAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdministrativeUnitFilterSet


class CaseAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.only("id", "name").all()
    serializer_class = CaseAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CaseFilterSet


class ChannelAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.only("id", "name").all()
    serializer_class = ChannelAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChannelFilterSet


class DocumentTypeAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentType.objects.only("id", "name").all()
    serializer_class = DocumentTypeAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DocumentTypeFilterSet


class EventAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.only("id", "name").all()
    serializer_class = EventAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilterSet


class FeatureAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feature.objects.only("id", "name").all()
    serializer_class = FeatureAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureFilterSet


class FeatureOptionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeatureOption.objects.only("id", "name").all()
    serializer_class = FeatureOptionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureOptionFilterSet


class InstitutionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.only("id", "name").all()
    serializer_class = InstitutionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstitutionFilterSet


class TagAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.only("id", "name").all()
    serializer_class = TagAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagFilterSet


class UserAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.only("id", "username").all()
    serializer_class = UserAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilterSet
