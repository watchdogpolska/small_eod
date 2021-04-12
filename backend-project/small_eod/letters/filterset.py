from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import DocumentType, Letter
from .searchset import DocumentTypeSearchSet, LetterSearchSet


class DocumentTypeFilterSet(FilterSet):
    query = SearchFilter(searchset=DocumentTypeSearchSet())

    class Meta:
        model = DocumentType
        fields = ["query"]


class LetterFilterSet(FilterSet):
    query = SearchFilter(searchset=LetterSearchSet())

    class Meta:
        model = Letter
        fields = ["query"]
