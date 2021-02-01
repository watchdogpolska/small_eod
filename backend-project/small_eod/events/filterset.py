from ..search.filter import SearchFilter
from .searchset import EventSearchSet
from .models import Event
from django_filters.filterset import FilterSet


class EventFilterSet(FilterSet):
    query = SearchFilter(searchset=EventSearchSet())

    class Meta:
        model = Event
        fields = ["query"]
