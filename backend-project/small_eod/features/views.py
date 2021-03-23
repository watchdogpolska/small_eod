from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Feature, FeatureOption
from .serializers import FeatureOptionSerializer, FeatureSerializer
from .filterset import FeatureFilterSet, FeatureOptionFilterSet


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.prefetch_related("featureoptions").all()
    serializer_class = FeatureSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = FeatureFilterSet
    ordering_fields = ["id", "name", "min_options", "max_options", "featureoptions"]


class FeatureOptionViewSet(viewsets.ModelViewSet):
    queryset = FeatureOption.objects.all()
    serializer_class = FeatureOptionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = FeatureOptionFilterSet
