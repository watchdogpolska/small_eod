from ..search.filter import SearchFilter
from .searchset import CaseSearchSet
from .models import Case
from django_filters.filterset import FilterSet


class CaseFilterSet(FilterSet):
    query = SearchFilter(searchset=CaseSearchSet())

    class Meta:
        model = Case
        fields = ["tags", "query"]
