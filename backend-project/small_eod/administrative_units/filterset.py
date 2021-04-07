from django_filters import FilterSet

from .models import AdministrativeUnit
from .searchset import AdministrativeUnitSearchSet
from ..search.filter import SearchFilter


class AdministrativeUnitFilterSet(FilterSet):
    query = SearchFilter(searchset=AdministrativeUnitSearchSet())

    class Meta:
        model = AdministrativeUnit
        fields = ["query"]