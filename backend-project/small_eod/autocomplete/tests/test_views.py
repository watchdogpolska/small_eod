from test_plus.test import TestCase

from ...administrative_units.factories import AdministrativeUnitFactory
from ...cases.factories import CaseFactory
from ...channels.factories import ChannelFactory
from ...events.factories import EventFactory
from ...features.factories import FeatureFactory, FeatureOptionFactory
from ...generic.tests.test_views import ReadOnlyViewSetMixin
from ...institutions.factories import InstitutionFactory
from ...letters.factories import DocumentTypeFactory, ReferenceNumberFactory
from ...search.tests.mixins import SearchQueryMixin
from ...tags.factories import TagFactory
from ...users.factories import UserFactory


class AdministrativeUnitAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_administrative_unit"
    factory_class = AdministrativeUnitFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class CaseAutocompleteViewSetTestCase(ReadOnlyViewSetMixin, SearchQueryMixin, TestCase):
    basename = "autocomplete_case"
    factory_class = CaseFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class ChannelAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_channel"
    factory_class = ChannelFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class DocumentTypeAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_document_type"
    factory_class = DocumentTypeFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class ReferenceNumberAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_reference_number"
    factory_class = ReferenceNumberFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class EventAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_event"
    factory_class = EventFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class FeatureAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_feature"
    factory_class = FeatureFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class FeatureOptionAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_feature_option"
    factory_class = FeatureOptionFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class InstitutionAutocompleteViewSetTestCase(
    ReadOnlyViewSetMixin, SearchQueryMixin, TestCase
):
    basename = "autocomplete_institution"
    factory_class = InstitutionFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class TagAutocompleteViewSetTestCase(ReadOnlyViewSetMixin, SearchQueryMixin, TestCase):
    basename = "autocomplete_tag"
    factory_class = TagFactory

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["name"], self.obj.name)


class UserAutocompleteViewSetTestCase(ReadOnlyViewSetMixin, SearchQueryMixin, TestCase):
    basename = "autocomplete_user"
    factory_class = UserFactory
    initial_count = 1

    def validate_item(self, item):
        self.assertEqual(item["id"], self.obj.id)
        self.assertEqual(item["username"], self.obj.username)
