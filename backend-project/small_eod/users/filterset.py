import rest_framework_filters as filters
from .models import User


class UserFilterSet(filters.FilterSet):
    username = filters.AutoFilter(lookups=["icontains"])

    class Meta:
        model = User
        fields = ["username"]
