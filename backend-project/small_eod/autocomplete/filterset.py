from django_filters import FilterSet
from ..search.filter import SearchFilter
from ..administrative_units.models import AdministrativeUnit
from ..cases.models import Case
from ..channels.models import Channel
from ..events.models import Event
from ..features.models import Feature, FeatureOption
from ..institutions.models import Institution
from ..letters.models import DocumentType, Letter
from ..notes.models import Note
from ..tags.models import Tag
from ..users.models import User
from ..administrative_units.searchset import AdministrativeUnitSearchSet
from ..cases.searchset import CaseSearchSet
from ..channels.searchset import ChannelSearchSet
from ..events.searchset import EventSearchSet
from ..features.searchset import FeatureSearchSet, FeatureOptionSearchSet
from ..institutions.searchset import InstitutionSearchSet
from ..letters.searchset import DocumentTypeSearchSet, LetterSearchSet
from ..notes.searchset import NoteSearchSet
from ..tags.searchset import TagSearchSet
from ..users.searchset import UserSearchSet


class AdministrativeUnitAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=AdministrativeUnitSearchSet())

    class Meta:
        model = AdministrativeUnit
        fields = ["query"]


class CaseAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=CaseSearchSet())

    class Meta:
        model = Case
        fields = ["query"]


class ChannelAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=ChannelSearchSet())

    class Meta:
        model = Channel
        fields = ["query"]


class DocumentTypeAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=DocumentTypeSearchSet())

    class Meta:
        model = DocumentType
        fields = ["query"]


class EventAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=EventSearchSet())

    class Meta:
        model = Event
        fields = ["query"]


class FeatureAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=FeatureSearchSet())

    class Meta:
        model = Feature
        fields = ["query"]


class FeatureOptionAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=FeatureOptionSearchSet())

    class Meta:
        model = FeatureOption
        fields = ["query"]


class InstitutionAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=InstitutionSearchSet())

    class Meta:
        model = Institution
        fields = ["query"]


class LetterAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=LetterSearchSet())

    class Meta:
        model = Letter
        fields = ["query"]


class NoteAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=NoteSearchSet())

    class Meta:
        model = Note
        fields = ["query"]


class TagAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=TagSearchSet())

    class Meta:
        model = Tag
        fields = ["query"]


class UserAutocompleteFilterSet(FilterSet):
    query = SearchFilter(searchset=UserSearchSet())

    class Meta:
        model = User
        fields = ["query"]
