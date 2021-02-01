from django.db.models import Q

from ..searchset import BaseSearchSet


class DemoSearchSet(BaseSearchSet):
    search_fields = ["name"]
    filters = {"a": lambda value: Q(a=value)}
