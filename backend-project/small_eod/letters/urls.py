from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    DocumentTypeViewSet,
    FileViewSet,
    LetterViewSet,
    PresignedUploadFileView,
)

router = routers.SimpleRouter()
router.register("letters", LetterViewSet, "letter")
router.register("documentTypes", DocumentTypeViewSet, "document_type")

file_router = routers.NestedSimpleRouter(router, "letters", lookup="letter")
file_router.register("files", FileViewSet, basename="letter-file")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(file_router.urls)),
    path("letters/files/sign", PresignedUploadFileView.as_view(), name="file_upload"),
]
