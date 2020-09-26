from django_filters.filters import CharFilter
from .field import SearchField


class SearchFilter(CharFilter):
    field_class = SearchField

    def __init__(self, *args, **kwargs):
        self.searchset = kwargs.pop("searchset")
        super().__init__(*args, **kwargs)

    def filter(self, qs, value):
        if not value:
            return qs
        return qs.filter(self.searchset.get_condition(value))
