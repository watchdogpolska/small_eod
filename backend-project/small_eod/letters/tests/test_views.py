from django.urls import reverse
from test_plus.test import TestCase
import requests
from io import BytesIO

from rest_framework import status
from rest_framework.test import APITestCase

from ..factories import LetterFactory
from ..serializers import LetterSerializer
from ...generic.tests.test_views import (
    GenericViewSetMixin,
    AuthorshipViewSetMixin,
    OrderingViewSetMixin,
)
from ...users.mixins import AuthenticatedMixin


class PresignedUploadFileTestCase(AuthenticatedMixin, APITestCase):
    def test_getting_form_data(self):
        self.login_required()
        url = reverse("file_upload")
        data = {"name": "text.file"}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("formData", response.data)

        form_data = response.data["formData"]
        self.assertIn("bucket", form_data)
        self.assertIn("key", form_data)
        self.assertIn("policy", form_data)
        self.assertIn("x-amz-algorithm", form_data)
        self.assertIn("x-amz-credential", form_data)
        self.assertIn("x-amz-date", form_data)
        self.assertIn("x-amz-signature", form_data)

    def test_file_upload_and_download(self):
        self.login_required()
        content = b"xxx"

        # Upload file
        backend_resp = self.client.post(
            path=reverse("file_upload"), data={"name": "text.file"}, format="json"
        )
        minio_upload_resp = requests.post(
            url=backend_resp.data["url"],
            data=backend_resp.data["formData"],
            files={"file": BytesIO(content)},
        )
        self.assertEqual(minio_upload_resp.status_code, status.HTTP_204_NO_CONTENT)

        # Create a file
        url = reverse("letter-file-list", kwargs={"letter_pk": LetterFactory().pk})

        response = self.client.post(url, backend_resp.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Download file content
        minio_download_resp = requests.get(url=response.json()["downloadUrl"])
        self.assertEqual(minio_download_resp.status_code, status.HTTP_200_OK)
        self.assertEqual(minio_download_resp.content, content)


class FileCreateTestCase(AuthenticatedMixin, APITestCase):
    def test_file_not_found(self):
        self.login_required()
        url = reverse("letter-file-list", kwargs={"letter_pk": 0})
        data = {"path": "path/to/file", "name": "test.file"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_file_created(self):
        self.login_required()
        letter = LetterFactory()

        url = reverse("letter-file-list", kwargs={"letter_pk": letter.pk})
        data = {"path": "path/to/file", "name": "test.file"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["path"], data["path"])
        self.assertIn("id", response.data)


class LetterViewSetTestCase(
    AuthorshipViewSetMixin, GenericViewSetMixin, OrderingViewSetMixin, TestCase
):
    basename = "letter"
    serializer_class = LetterSerializer
    factory_class = LetterFactory
    queries_less_than_limit = 10
    ordering_fields = [
        "comment",
        "-comment",
        "created_on",
        "created_by__username",
        "-created_by__username,comment",
    ]

    def validate_item(self, item):
        self.assertEqual(item["comment"], self.obj.comment)
        self.assertEqual(item["documentType"], self.obj.document_type.pk)

    def test_create_minimum(self):
        self.login_required()
        comment = "testowy-opis"
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data={"comment": comment},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertEqual(item["comment"], comment)

    def get_update_data(self):
        return {"comment": f"{self.obj.comment}-updated"}

    def validate_update_item(self, item):
        self.assertEqual(item["id"], self.obj.pk)
        self.assertEqual(item["comment"], f"{self.obj.comment}-updated")
