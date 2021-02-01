from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg2.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView

from ..files.models import File
from ..files.serializers import FileSerializer
from .models import DocumentType, Letter
from .serializers import DocumentTypeSerializer, LetterSerializer, SignRequestSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.prefetch_related("attachments").all()
    serializer_class = LetterSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = [
        "id",
        "direction",
        "channel__name",
        "final",
        "date",
        "reference_number",
        "institution__name",
        "case__name",
        "attachments",
        "comment",
        "excerpt",
        "document_type__name",
        "created_on",
        "created_by__username",
        "modified_on",
        "modified_by__username",
    ]


class DocumentTypeViewSet(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer


class FileViewSet(
    viewsets.ModelViewSet,
    viewsets.GenericViewSet,
):
    model = File
    serializer_class = FileSerializer

    def get_queryset(self):
        return self.model.objects.filter(letter__pk=self.kwargs["letter_pk"]).all()

    def perform_create(self, serializer):
        serializer.save(letter=get_object_or_404(Letter, pk=self.kwargs["letter_pk"]))


class PresignedUploadFileView(APIView):
    """
    Generates pre-signed form data for uploading files to object storage.
    """

    serializer_class = SignRequestSerializer

    @swagger_auto_schema(request_body=SignRequestSerializer)
    def post(self, request, format=None):
        serializer = SignRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Trigger .create(..)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
