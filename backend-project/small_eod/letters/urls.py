from rest_framework_nested import routers
from .views import (
    LetterViewSet,
    FileViewSet,
    PresignedUploadFileView,
    DocumentTypeViewSet,
)

from django.urls import path, include

router = routers.SimpleRouter()
router.register("letters", LetterViewSet)
router.register("documentTypes", DocumentTypeViewSet)

file_router = routers.NestedSimpleRouter(router, "letters", lookup="letter")
file_router.register("files", FileViewSet, basename="letter-file")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(file_router.urls)),
    path("letters/files/sign", PresignedUploadFileView.as_view(), name="file_upload"),
]
