from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .filterset import (
    AdministrativeUnitAutocompleteFilterSet,
    CaseAutocompleteFilterSet,
    ChannelAutocompleteFilterSet,
    DocumentTypeAutocompleteFilterSet,
    FeatureAutocompleteFilterSet,
    FeatureOptionAutocompleteFilterSet,
    InstitutionAutocompleteFilterSet,
    TagAutocompleteFilterSet,
    UserAutocompleteFilterSet,
)
from .serializers import (
    AdministrativeUnitAutocompleteSerializer,
    CaseAutocompleteSerializer,
    ChannelAutocompleteSerializer,
    DocumentTypeAutocompleteSerializer,
    FeatureAutocompleteSerializer,
    FeatureOptionAutocompleteSerializer,
    InstitutionAutocompleteSerializer,
    TagAutocompleteSerializer,
    UserAutocompleteSerializer,
)
from ..administrative_units.models import AdministrativeUnit
from ..cases.models import Case, Tag
from ..channels.models import Channel
from ..features.models import Feature, FeatureOption
from ..institutions.models import Institution
from ..letters.models import DocumentType
from ..users.models import User


class AdministrativeUnitAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdministrativeUnit.objects.all()
    serializer_class = AdministrativeUnitAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdministrativeUnitAutocompleteFilterSet


class CaseAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CaseAutocompleteFilterSet


class ChannelAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChannelAutocompleteFilterSet


class DocumentTypeAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DocumentTypeAutocompleteFilterSet


class FeatureAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureAutocompleteFilterSet


class FeatureOptionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FeatureOption.objects.all()
    serializer_class = FeatureOptionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FeatureOptionAutocompleteFilterSet


class InstitutionAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstitutionAutocompleteFilterSet


class TagsAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagAutocompleteFilterSet


class UserAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserAutocompleteFilterSet
