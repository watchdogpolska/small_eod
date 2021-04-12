from django.db.models import Q

from ..search.searchset import BaseSearchSet


class DocumentTypeSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {
        "id": lambda value: Q(pk=value),
    }


class LetterSearchSet(BaseSearchSet):
    search_fields = ["comment"]
    filters = {
        "id": lambda value: Q(pk=value),
        "tag": lambda value: Q(tag__name=value),
        "case": lambda value: Q(case__pk=value),
        "institution": lambda value: Q(institution__pk=value),
    }
