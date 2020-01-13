from rest_framework import viewsets

from .models import Case
from .serializers import CaseCountSerializer
from ..users.serializers import UserSerializer


class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.with_counter().all()
    serializer_class = CaseCountSerializer


class ResponsibleUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return Case.objects.get(pk=self.kwargs['case_pk']).responsible_user.all()


class NotifiedUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return Case.objects.get(pk=self.kwargs['case_pk']).notified_user.all()
