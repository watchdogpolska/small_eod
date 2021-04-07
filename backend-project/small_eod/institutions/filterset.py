from django_filters.filterset import FilterSet
from ..search.filter import SearchFilter
from .models import Institution
from .searchset import InstitutionSearchSet


class InstitutionFilterSet(FilterSet):
    query = SearchFilter(searchset=InstitutionSearchSet())

    class Meta:
        model = Institution
        fields = ["name", "query"]
