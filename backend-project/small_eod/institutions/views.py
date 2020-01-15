from rest_framework import viewsets

from .serializers import InstitutionSerializer
from .models import Institution


class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
