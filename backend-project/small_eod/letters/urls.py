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
router.register("document_types", DocumentTypeViewSet)

file_router = routers.NestedSimpleRouter(router, "letters", lookup="letter")
file_router.register("files", FileViewSet, basename="letter-files")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(file_router.urls)),
    path("letters/file/sign", PresignedUploadFileView.as_view(), name="file_upload"),
]
