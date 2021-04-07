from django_filters.filterset import FilterSet

from ..search.filter import SearchFilter
from .models import Feature, FeatureOption
from .searchset import FeatureOptionSearchSet, FeatureSearchSet


class FeatureFilterSet(FilterSet):
    query = SearchFilter(searchset=FeatureSearchSet())

    class Meta:
        model = Feature
        fields = ["query"]


class FeatureOptionFilterSet(FilterSet):
    query = SearchFilter(searchset=FeatureOptionSearchSet())

    class Meta:
        model = FeatureOption
        fields = ["query"]
