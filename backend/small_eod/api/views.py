from rest_framework import viewsets
from django.contrib.auth import get_user_model
from institution.models import AddressData, Institution
from case.models import Case
from api.serializers import UserSerializer, AddressDataSerializer, InstitutionSerializer, CaseSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class AddressDataViewSet(viewsets.ModelViewSet):
    queryset = AddressData.objects.all()
    serializer_class = AddressDataSerializer


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
