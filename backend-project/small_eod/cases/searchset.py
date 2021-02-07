from django.db.models import Q

from ..search.searchset import BaseSearchSet


class CaseSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {
        "id": lambda value: Q(pk=value),
        "tag": lambda value: Q(tag__name=value),
    }
