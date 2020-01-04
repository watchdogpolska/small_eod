from rest_framework import viewsets

from .serializers import CaseSerializer, Case


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer
