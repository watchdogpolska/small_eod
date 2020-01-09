from rest_framework import viewsets

from .models import Case
from .serializers import CaseCountSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.with_counter().all()
    serializer_class = CaseCountSerializer
