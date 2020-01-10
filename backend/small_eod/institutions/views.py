from rest_framework import viewsets

from .serializers import AddressDataSerializer, InstitutionSerializer
from .models import AddressData, Institution


class AddressDataViewSet(viewsets.ModelViewSet):
    queryset = AddressData.objects.all()
    serializer_class = AddressDataSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
