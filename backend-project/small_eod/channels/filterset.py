from django_filters import FilterSet

from ..search.filter import SearchFilter
from .models import Channel
from .searchset import ChannelSearchSet


class ChannelFilterSet(FilterSet):
    query = SearchFilter(searchset=ChannelSearchSet())

    class Meta:
        model = Channel
        fields = ["query"]
