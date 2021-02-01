from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg2 import openapi
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .filterset import InstitutionFilterSet
from .models import Institution
from .serializers import InstitutionSerializer


@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name="query",
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description="Query filter. Currently filtering by name.",
            )
        ]
    ),
)
class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = InstitutionFilterSet
    ordering_fields = [
        "id",
        "modified_by__username",
        "created_by__username",
        "modified_on",
        "created_on",
        "name",
        "administrative_unit__name",
        "email",
        "city",
        "epuap",
        "street",
        "house_no",
        "postal_code",
        "flat_no",
        "nip",
        "regon",
        "comment",
        "tags__name",
    ]
