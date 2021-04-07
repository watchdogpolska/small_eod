from django_filters.filterset import FilterSet
from ..search.filter import SearchFilter
from .models import Case
from .searchset import CaseSearchSet


class CaseFilterSet(FilterSet):
    query = SearchFilter(searchset=CaseSearchSet())

    class Meta:
        model = Case
        fields = ["query"]
