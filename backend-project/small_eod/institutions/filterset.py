from ..search.filter import SearchFilter
from .searchset import InstitutionSearchSet
from .models import Institution
from django_filters.filterset import FilterSet


class InstitutionFilterSet(FilterSet):
    query = SearchFilter(searchset=InstitutionSearchSet())

    class Meta:
        model = Institution
        fields = ["query"]
