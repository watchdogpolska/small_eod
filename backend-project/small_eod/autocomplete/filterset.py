import rest_framework_filters as filters

from ..administrative_units.models import AdministrativeUnit
from ..cases.models import Case, Tag
from ..channels.models import Channel
from ..features.models import Feature, FeatureOption
from ..institutions.models import Institution
from ..letters.models import DocumentType
from ..users.models import User


class AdministrativeUnitAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = AdministrativeUnit
        fields = ["id", "name"]


class CaseAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Case
        fields = ["id", "name"]


class ChannelAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Channel
        fields = ["id", "name"]


class DocumentTypeAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = DocumentType
        fields = ["id", "name"]


class FeatureAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Feature
        fields = ["id", "name"]


class FeatureOptionAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = FeatureOption
        fields = ["id", "name"]


class InstitutionAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Institution
        fields = ["id", "name"]


class TagAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Tag
        fields = ["id", "name"]


class UserAutocompleteFilterSet(filters.FilterSet):
    id = filters.AutoFilter(lookups=["in"])
    username = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = User
        fields = ["id", "username"]
