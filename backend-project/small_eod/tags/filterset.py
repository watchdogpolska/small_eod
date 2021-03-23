import rest_framework_filters as filters
from .models import Tag


class TagFilter(filters.FilterSet):
    name = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = Tag
        fields = ["name"]