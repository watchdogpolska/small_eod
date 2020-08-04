from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
    ]
