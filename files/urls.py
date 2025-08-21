from django.urls import path
from .views import (
    FileUploadView,
    FileProgressView,
    FileContentView,
    FileListView,
    FileDeleteView,
)

urlpatterns = [
    path("files/", FileListView.as_view(), name="file-list"),
    path("files/upload/", FileUploadView.as_view(), name="file-upload"),
    path("files/<uuid:pk>/progress/", FileProgressView.as_view(), name="file-progress"),
    path("files/<uuid:pk>/", FileContentView.as_view(), name="file-content"),
    path("files/<uuid:pk>/delete/", FileDeleteView.as_view(), name="file-delete"),
]
