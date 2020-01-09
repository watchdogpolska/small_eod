from rest_framework import viewsets

from .serializers import TagSerializer, Tag


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
