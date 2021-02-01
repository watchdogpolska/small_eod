from ..search.filter import SearchFilter
from .searchset import NoteSearchSet
from .models import Note
from django_filters.filterset import FilterSet


class NoteFilterSet(FilterSet):
    query = SearchFilter(searchset=NoteSearchSet())

    class Meta:
        model = Note
        fields = ["query"]
