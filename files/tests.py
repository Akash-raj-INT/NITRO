from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile


class FileUploadTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_file_upload(self):
        file = SimpleUploadedFile("test.txt", b"hello world", content_type="text/plain")
        url = reverse("file-upload")
        response = self.client.post(url, {"file": file}, format="multipart")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_files(self):
        url = reverse("file-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
