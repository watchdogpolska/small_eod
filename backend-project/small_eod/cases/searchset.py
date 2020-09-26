from ..search.searchset import BaseSearchSet
from django.db.models import Q


class CaseSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {"id": lambda value: Q(pk=value)}
