from django.db.models import Q

from ..search.searchset import BaseSearchSet


class EventSearchSet(BaseSearchSet):
    search_fields = ["name", "comment"]
    filters = {
        "id": lambda value: Q(pk=value),
        "case": lambda value: Q(case__pk=value),
    }
