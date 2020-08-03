from rest_framework import viewsets
from .models import Feature, FeatureOption
from .serializers import FeatureSerializer, FeatureOptionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.prefetch_related("featureoptions").all()
    serializer_class = FeatureSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ["id", "name", "min_options", "max_options", "featureoptions"]


class FeatureOptionViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureOptionSerializer
    model = FeatureOption

    def get_queryset(self):
        return self.model.objects.filter(feature=self.kwargs["feature_pk"])
