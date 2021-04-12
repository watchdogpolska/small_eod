from django_filters import FilterSet

from ..search.filter import SearchFilter
from .models import AdministrativeUnit
from .searchset import AdministrativeUnitSearchSet


class AdministrativeUnitFilterSet(FilterSet):
    query = SearchFilter(searchset=AdministrativeUnitSearchSet())

    class Meta:
        model = AdministrativeUnit
        fields = ["query"]
