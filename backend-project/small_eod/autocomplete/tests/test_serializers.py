from django.test import TestCase

from ...administrative_units.factories import AdministrativeUnitFactory
from ...cases.factories import CaseFactory
from ...channels.factories import ChannelFactory
from ...events.factories import EventFactory
from ...features.factories import FeatureFactory, FeatureOptionFactory
from ...generic.mixins import AuthRequiredMixin
from ...generic.tests.test_serializers import ResourceSerializerMixin
from ...institutions.factories import InstitutionFactory
from ...letters.factories import DocumentTypeFactory, ReferenceNumberFactory
from ...tags.factories import TagFactory
from ...users.factories import UserFactory
from ..serializers import (
    AdministrativeUnitAutocompleteSerializer,
    CaseAutocompleteSerializer,
    ChannelAutocompleteSerializer,
    DocumentTypeAutocompleteSerializer,
    EventAutocompleteSerializer,
    FeatureAutocompleteSerializer,
    FeatureOptionAutocompleteSerializer,
    InstitutionAutocompleteSerializer,
    ReferenceNumberAutocompleteSerializer,
    TagAutocompleteSerializer,
    UserAutocompleteSerializer,
)


class AdministrativeUnitAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = AdministrativeUnitAutocompleteSerializer
    factory_class = AdministrativeUnitFactory


class CaseAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = CaseAutocompleteSerializer
    factory_class = CaseFactory


class ChannelAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = ChannelAutocompleteSerializer
    factory_class = ChannelFactory


class DocumentTypeAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = DocumentTypeAutocompleteSerializer
    factory_class = DocumentTypeFactory


class ReferenceNumberAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = ReferenceNumberAutocompleteSerializer
    factory_class = ReferenceNumberFactory


class EventAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = EventAutocompleteSerializer
    factory_class = EventFactory


class FeatureAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = FeatureAutocompleteSerializer
    factory_class = FeatureFactory


class FeatureOptionAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = FeatureOptionAutocompleteSerializer
    factory_class = FeatureOptionFactory


class InstitutionAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = InstitutionAutocompleteSerializer
    factory_class = InstitutionFactory


class TagAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = TagAutocompleteSerializer
    factory_class = TagFactory


class UserAutocompleteSerializerTestCase(
    ResourceSerializerMixin, AuthRequiredMixin, TestCase
):
    serializer_class = UserAutocompleteSerializer
    factory_class = UserFactory
