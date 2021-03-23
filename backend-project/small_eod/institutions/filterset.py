import rest_framework_filters as filters
from ..search.filter import SearchFilter
from .models import Institution
from .searchset import InstitutionSearchSet


class InstitutionFilterSet(filters.FilterSet):
    query = SearchFilter(searchset=InstitutionSearchSet())
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Institution
        fields = ["name", "query"]
