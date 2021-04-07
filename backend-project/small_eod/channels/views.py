from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter

from .models import Channel
from .serializers import ChannelSerializer
from .filterset import ChannelFilterSet


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = ChannelFilterSet
    ordering_fields = [
        "id",
        "name",
        "city",
        "voivodeship",
        "flat_no",
        "street",
        "postal_code",
        "house_no",
        "email",
        "epuap",
    ]
