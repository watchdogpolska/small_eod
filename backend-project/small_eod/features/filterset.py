import rest_framework_filters as filters
from .models import Feature, FeatureOption


class FeatureFilterSet(filters.FilterSet):
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Feature
        fields = ["name"]


class FeatureOptionFilterSet(filters.FilterSet):
    name = filters.AutoFilter(lookups=["icontains"])
    feature = filters.ModelChoiceFilter(queryset=Feature.objects.all())

    class Meta:
        model = FeatureOption
        fields = ["name", "feature"]
