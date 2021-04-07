from django_filters.filterset import FilterSet
from .models import Tag


class TagFilter(FilterSet):
    class Meta:
        model = Tag
        fields = ["name"]
