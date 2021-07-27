from django_filters.rest_framework import DjangoFilterBackend
from django.db import models
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
from ..letters.filterset import DocumentTypeFilterSet, ReferenceNumberFilterSet
from ..letters.models import DocumentType, ReferenceNumber, Letter
from ..tags.filterset import TagFilterSet
from ..tags.models import Tag
from ..users.filterset import UserFilterSet
from ..users.models import User
from .serializers import (
    AdministrativeUnitAutocompleteSerializer,
    CaseAutocompleteSerializer,
    ChannelAutocompleteSerializer,
    DocumentTypeAutocompleteSerializer,
    ReferenceNumberAutocompleteSerializer,
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


class ReferenceNumberAutocompleteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ReferenceNumberAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReferenceNumberFilterSet

    def get_queryset(self):
        req = self.request
        related_case_id = req.GET.get("case", None)
        if related_case_id is None:
            qs = ReferenceNumber.objects.all()
        else:
            # Put related objects at the beginning of the list.
            reference_numbers_under_case = (
                Letter.objects.filter(case=related_case_id)
                .values_list("reference_number", flat=True)
                .distinct()
            )
            qs = ReferenceNumber.objects.annotate(
                related=models.Case(
                    models.When(id__in=reference_numbers_under_case, then=True),
                    default=False,
                    output_field=models.BooleanField(),
                )
            ).order_by("-related")
        return qs.only("id", "name")


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
    serializer_class = InstitutionAutocompleteSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = InstitutionFilterSet

    def get_queryset(self):
        req = self.request
        related_case_id = req.GET.get("case", None)
        if related_case_id is None:
            qs = Institution.objects.all()
        else:
            # Put related institutions at the beginning of the list.
            qs = Institution.objects.annotate(
                related=models.Case(
                    models.When(case=related_case_id, then=True),
                    default=False,
                    output_field=models.BooleanField(),
                )
            ).order_by("-related")
        return qs.only("id", "name")


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
