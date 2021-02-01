from ..search.searchset import BaseSearchSet
from django.db.models import Q


class NoteSearchSet(BaseSearchSet):
    search_fields = ["name", "comment"]
    filters = {
        "id": lambda value: Q(pk=value),
        "case": lambda value: Q(case__pk=value),
    }
