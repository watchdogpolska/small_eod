from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .models import Collection
from .serializers import CollectionSerializer, TokenSetSerializer
from ..cases.serializers import CaseSerializer
from ..cases.models import Case
from ..notes.serializers import NoteSerializer
from ..notes.models import Note
from ..events.serializers import EventSerializer
from ..events.models import Event
from ..letters.serializers import LetterSerializer
from ..letters.models import Letter
from django.shortcuts import get_object_or_404
from .permissions import (
    CollectionMemberTokenPermission,
    CollectionDirectTokenPermission,
)
from django.conf import settings

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


class CaseViewSet(CollectionTokenSecuredViewSet):
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
        return self.model.objects.filter(case=case).all()


class EventViewSet(BaseSubCollection):
    serializer_class = EventSerializer
    model = Event


class NoteViewSet(BaseSubCollection):
    serializer_class = NoteSerializer
    model = Note


class LetterViewSet(BaseSubCollection):
    serializer_class = LetterSerializer
    model = Letter
