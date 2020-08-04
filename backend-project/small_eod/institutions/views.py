from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .serializers import InstitutionSerializer
from .models import Institution


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

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("query")
        if query:
            qs = qs.filter(name__icontains=query)
        return qs
