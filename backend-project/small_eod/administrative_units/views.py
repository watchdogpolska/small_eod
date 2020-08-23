from rest_framework import viewsets

from .models import AdministrativeUnit
from .serializers import AdministrativeUnitSerializer


class AdministrativeUnitViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AdministrativeUnit.objects.all()
    serializer_class = AdministrativeUnitSerializer
