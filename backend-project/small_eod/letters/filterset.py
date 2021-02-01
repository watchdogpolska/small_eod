from ..search.filter import SearchFilter
from .searchset import LetterSearchSet
from .models import Letter
from django_filters.filterset import FilterSet


class LetterFilterSet(FilterSet):
    query = SearchFilter(searchset=LetterSearchSet())

    class Meta:
        model = Letter
        fields = ["query"]
