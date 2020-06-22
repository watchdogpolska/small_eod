from rest_framework import viewsets

from .models import JednostkaAdministracyjna
from .serializers import AdministrativeUnitSerializer
from ..users.serializers import UserSerializer


class JednostkaAdministracyjnaViewSet(viewsets.ModelViewSet):
    queryset = JednostkaAdministracyjna.objects.all()
    serializer_class = AdministrativeUnitSerializer
