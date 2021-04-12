from django.db.models import Q

from ..search.searchset import BaseSearchSet


class AdministrativeUnitSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {
        "id": lambda value: Q(pk=value),
    }
