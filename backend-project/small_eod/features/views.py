from rest_framework import viewsets
from .models import Feature, FeatureOption
from .serializers import FeatureSerializer, FeatureOptionSerializer


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class FeatureOptionViewSet(viewsets.ModelViewSet):
    serializer_class = FeatureOptionSerializer
    model = FeatureOption

    def get_queryset(self):
        return self.model.objects.filter(feature=self.kwargs["feature_pk"])
