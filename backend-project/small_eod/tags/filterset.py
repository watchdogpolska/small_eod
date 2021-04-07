from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import Tag
from .searchset import TagSearchSet


class TagFilterSet(FilterSet):
    query = SearchFilter(searchset=TagSearchSet())

    class Meta:
        model = Tag
        fields = ["query"]
