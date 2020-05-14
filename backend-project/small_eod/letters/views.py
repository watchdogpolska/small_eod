from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Letter, Description
from .serializers import (
    LetterSerializer,
    DescriptionSerializer,
    SignRequestSerializer,
)
from ..files.serializers import FileSerializer
from ..files.models import File


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class FileViewSet(
    viewsets.ModelViewSet, viewsets.GenericViewSet,
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
