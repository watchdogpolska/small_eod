from rest_framework import viewsets

from .models import JednostkaAdministracyjna
from .serializers import AdministrativeUnitSerializer


class JednostkaAdministracyjnaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = JednostkaAdministracyjna.objects.all()
    serializer_class = AdministrativeUnitSerializer
