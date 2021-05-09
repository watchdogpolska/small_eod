from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from ..notifications.views import SendNotificationsMixin
from ..users.serializers import UserSerializer
from .filterset import CaseFilterSet
from .models import Case
from .serializers import CaseCountSerializer


class CaseViewSet(viewsets.ModelViewSet, SendNotificationsMixin):
    queryset = Case.objects.with_counter().with_nested_resources().all()
    serializer_class = CaseCountSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CaseFilterSet
    ordering_fields = [
        "id",
        "comment",
        "audited_institutions__name",
        "name",
        "responsible_users__username",
        "notified_users__username",
        "featureoptions__name",
        "tags__name",
        "created_by__username",
        "modified_by__username",
        "created_on",
        "modified_on",
    ]
    notified_users = "notified_users"


class ResponsibleUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    )

    def get_queryset(self):
        return Case.objects.get(pk=self.kwargs["case_pk"]).responsible_users.all()


class NotifiedUserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    )

    def get_queryset(self):
        return Case.objects.get(pk=self.kwargs["case_pk"]).notified_users.all()
