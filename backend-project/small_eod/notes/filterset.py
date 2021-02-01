from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import Note
from .searchset import NoteSearchSet


class NoteFilterSet(FilterSet):
    query = SearchFilter(searchset=NoteSearchSet())

    class Meta:
        model = Note
        fields = ["query"]
