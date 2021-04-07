from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .filterset import AdministrativeUnitFilterSet
from .models import AdministrativeUnit
from .serializers import AdministrativeUnitSerializer


class AdministrativeUnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdministrativeUnit.objects.prefetch_related("category").all()
    serializer_class = AdministrativeUnitSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AdministrativeUnitFilterSet
    ordering_fields = [
        "id",
        "category__level",
        "name",
        "updated_on",
        "active",
    ]
