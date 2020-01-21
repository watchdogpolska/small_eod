from django.test import TestCase
from django.urls import reverse

from .factories import DescriptionFactory, LetterFactory
from .models import Description, Letter
from ..generic.tests import FactoryCreateObjectsMixin

from rest_framework import status
from rest_framework.test import APITestCase


class LetterFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = LetterFactory
    MODEL = Letter


class DescriptionFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = DescriptionFactory
    MODEL = Description


class PresignedUploadFileTestCase(APITestCase):
    def test_getting_form_data(self):
        url = reverse('file_upload')
        data = {
            'name': 'text.file',
        }

        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_not_allowed(self):
        url = reverse('file_upload')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class FileCreateTestCase(APITestCase):
    def test_file_not_found(self):
        url = reverse('create_file', kwargs={'letter_id': 0})
        data = {
            'path': 'path/to/file',
            'name': 'test.file'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_file_created(self):
        letter = LetterFactory()

        url = reverse('create_file', kwargs={'letter_id': letter.id})
        data = {
            'path': 'path/to/file',
            'name': 'test.file'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])
        self.assertEqual(response.data['path'], data['path'])
        self.assertIn('id', response.data)

    def test_get_not_allowed(self):
        url = reverse('create_file', kwargs={'letter_id': 0})

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
