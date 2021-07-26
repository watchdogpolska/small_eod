from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..cases.models import Case
from ..cases.serializers import CaseSerializer
from ..events.models import Event
from ..events.serializers import EventSerializer
from ..letters.models import Letter
from ..letters.serializers import LetterSerializer
from ..notes.models import Note
from ..notes.serializers import NoteSerializer
from .models import Collection
from .permissions import (
    CollectionDirectTokenPermission,
    CollectionMemberTokenPermission,
)
from .serializers import CollectionSerializer, TokenSetSerializer

SECURITY_SCHEMAS = list(settings.SWAGGER_SETTINGS["SECURITY_REQUIREMENTS"]) + [
    {"CollectionToken": []}
]

security_decorator = swagger_auto_schema(security=SECURITY_SCHEMAS)


def parse_query(query):
    # TODO: Add extensive query parser
    return {"pk__in": [int(x) for x in query.split(",")]}


@method_decorator(name="retrieve", decorator=security_decorator)
class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated | CollectionDirectTokenPermission]
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = ["id", "name", "comment", "public", "expired_on", "query"]


class TokenCreateAPIView(APIView):
    serializer_class = TokenSetSerializer

    @swagger_auto_schema(
        request_body=TokenSetSerializer,
        decorator=swagger_auto_schema(
            request_body=TokenSetSerializer, security=SECURITY_SCHEMAS
        ),
    )
    def post(self, request, collection_pk):
        collection = get_object_or_404(Collection, pk=collection_pk)
        serializer = TokenSetSerializer(
            data=self.request.data,
            context={"collection": collection, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        tokenset = serializer.save(collection=collection)
        return Response(tokenset, status=status.HTTP_201_CREATED)


@method_decorator(name="list", decorator=security_decorator)
@method_decorator(name="retrieve", decorator=security_decorator)
class CollectionTokenSecuredViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated | CollectionMemberTokenPermission]


class CaseCollectionViewSet(CollectionTokenSecuredViewSet):
    serializer_class = CaseSerializer

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        return (
            Case.objects.filter(**parse_query(collection.query))
            .with_counter()
            .with_nested_resources()
            .all()
        )


class BaseSubCollection(CollectionTokenSecuredViewSet):
    model = None

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        case = Case.objects.filter(**parse_query(collection.query)).get(
            pk=self.kwargs["case_pk"]
        )
        return self.model.objects.filter(case=case).with_nested_resources().all()


class EventCollectionViewSet(BaseSubCollection):
    serializer_class = EventSerializer
    model = Event


class NoteCollectionViewSet(BaseSubCollection):
    serializer_class = NoteSerializer
    model = Note


class LetterCollectionViewSet(BaseSubCollection):
    serializer_class = LetterSerializer
    model = Letter
