from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

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


def parse_query(query):
    # TODO: Add extensive query parser
    return {"pk__in": [int(x) for x in query.split(",")]}


class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticated | CollectionDirectTokenPermission]


class TokenCreateAPIView(APIView):
    serializer_class = TokenSetSerializer

    @swagger_auto_schema(request_body=TokenSetSerializer)
    def post(self, request, collection_pk):
        collection = get_object_or_404(Collection, pk=collection_pk)
        serializer = TokenSetSerializer(
            data=self.request.data,
            context={"collection": collection, "request": request},
        )
        serializer.is_valid(raise_exception=True)
        tokenset = serializer.save(collection=collection)
        return Response(tokenset, status=status.HTTP_201_CREATED)


class CaseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CaseSerializer
    permission_classes = [IsAuthenticated | CollectionMemberTokenPermission]

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        return Case.objects.filter(**parse_query(collection.queries)).with_counter().all()


class BaseSubCollection(viewsets.ReadOnlyModelViewSet):
    model = None
    permission_classes = [IsAuthenticated | CollectionMemberTokenPermission]

    def get_queryset(self):
        collection = Collection.objects.get(pk=self.kwargs["collection_pk"])
        case = Case.objects.filter(**parse_query(collection.queries)).get(
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
