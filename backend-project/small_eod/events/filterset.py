from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import Event
from .searchset import EventSearchSet


class EventFilterSet(FilterSet):
    query = SearchFilter(searchset=EventSearchSet())

    class Meta:
        model = Event
        fields = ["query"]
