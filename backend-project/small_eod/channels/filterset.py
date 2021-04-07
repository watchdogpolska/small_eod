from django_filters import FilterSet

from .models import Channel
from .searchset import ChannelSearchSet
from ..search.filter import SearchFilter


class ChannelFilterSet(FilterSet):
    query = SearchFilter(searchset=ChannelSearchSet())

    class Meta:
        model = Channel
        fields = ["query"]