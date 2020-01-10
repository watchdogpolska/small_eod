from rest_framework import viewsets

from .serializers import AddressDataSerializer, InstitutionSerializer
from .models import AddressData, Institution


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
