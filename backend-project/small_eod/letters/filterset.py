from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import Letter
from .searchset import LetterSearchSet


class LetterFilterSet(FilterSet):
    query = SearchFilter(searchset=LetterSearchSet())

    class Meta:
        model = Letter
        fields = ["query"]
