from django.db.models import Q

from ..search.searchset import BaseSearchSet


class FeatureSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {
        "id": lambda value: Q(pk=value),
    }


class FeatureOptionSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {
        "id": lambda value: Q(pk=value),
    }
