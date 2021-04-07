from django_filters.filterset import FilterSet

from .models import User


class UserFilterSet(FilterSet):
    class Meta:
        model = User
        fields = ["username"]
