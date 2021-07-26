from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import DocumentType, Letter, ReferenceNumber
from .searchset import DocumentTypeSearchSet, LetterSearchSet, ReferenceNumberSearchSet


class DocumentTypeFilterSet(FilterSet):
    query = SearchFilter(searchset=DocumentTypeSearchSet())

    class Meta:
        model = DocumentType
        fields = ["query"]


class ReferenceNumberFilterSet(FilterSet):
    query = SearchFilter(searchset=ReferenceNumberSearchSet())

    class Meta:
        model = ReferenceNumber
        fields = ["query"]


class LetterFilterSet(FilterSet):
    query = SearchFilter(searchset=LetterSearchSet())

    class Meta:
        model = Letter
        fields = ["query"]
