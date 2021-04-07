from django_filters.filterset import FilterSet
from .models import Feature, FeatureOption


class FeatureFilterSet(FilterSet):
    class Meta:
        model = Feature
        fields = ["name"]


class FeatureOptionFilterSet(FilterSet):
    class Meta:
        model = FeatureOption
        fields = ["name", "feature"]
