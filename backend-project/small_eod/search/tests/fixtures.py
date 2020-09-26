from ..searchset import BaseSearchSet
from django.db.models import Q


class DemoSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {"a": lambda value: Q(a=value)}
