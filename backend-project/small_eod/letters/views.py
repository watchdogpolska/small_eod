from uuid import uuid4
from urllib.parse import urljoin

from django.shortcuts import get_object_or_404, redirect

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Letter, Description
from .serializers import LetterSerializer, DescriptionSerializer

from config.minio_app import minio_app
from small_eod.files.serializers import FileSerializer, FileRelatedSerializer
from ..files.models import File


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer


class DescriptionViewSet(viewsets.ModelViewSet):
    queryset = Description.objects.all()
    serializer_class = DescriptionSerializer


class PresignedUploadFileView(APIView):
    """
    Generates presigned form data for uploading files.

    """
    def post(self, request, format=None):
        name = request.data['name']
        path = f'{uuid4()}/{name}'
        url, form_data = minio_app.presigned_post_form_data('files', f'{uuid4()}/{name}')
        path = urljoin(url, path)

        return Response({
            'name': name,
            'method': 'POST',
            'url': url,
            'formData': form_data,
            'path': path,
        }, status=status.HTTP_201_CREATED)


class CreateFileView(APIView):
    """
    Creates File instance within Letter.

    """
    def post(self, request, letter_id, format=None):
        get_object_or_404(Letter, id=letter_id)
        serializer = FileRelatedSerializer(data={
            'path': request.data['path'],
            'name': request.data['name'],
            'letter': letter_id,
        })

        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            del response_data['letter']  # To be compliant with swagger
            return Response(response_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_letter_file(request, letter_id, file_id):
    """
    Redirects to already existing view.

    """

    return redirect('letter-detail', pk=letter_id)
