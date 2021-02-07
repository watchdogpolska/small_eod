from django.db.models import Q

from ..search.searchset import BaseSearchSet


class LetterSearchSet(BaseSearchSet):
    search_fields = ["name", "comment"]
    filters = {
        "id": lambda value: Q(pk=value),
        "tag": lambda value: Q(tag__name=value),
        "case": lambda value: Q(case__pk=value),
        "institution": lambda value: Q(institution__pk=value),
    }
