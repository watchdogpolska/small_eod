from django.db.models import Q

from ..search.searchset import BaseSearchSet


class UserSearchSet(BaseSearchSet):
    search_fields = ["username"]
    filters = {
        "id": lambda value: Q(pk=value),
    }
