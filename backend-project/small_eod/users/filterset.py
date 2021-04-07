from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import User
from .searchset import UserSearchSet


class UserFilterSet(FilterSet):
    query = SearchFilter(searchset=UserSearchSet())

    class Meta:
        model = User
        fields = ["query"]
