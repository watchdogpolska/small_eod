from rest_framework_nested import routers
from .views import (
    CollectionViewSet,
    CaseViewSet,
    EventViewSet,
    LetterViewSet,
    NoteViewSet,
)

from django.urls import path, re_path, include

router = routers.SimpleRouter()
router.register("collections", CollectionViewSet)

case_router = routers.NestedSimpleRouter(router, "collections", lookup="collection")
case_router.register("case", CaseViewSet, basename="collection-cases")

event_router = routers.NestedSimpleRouter(case_router, "case", lookup="case")
event_router.register("event", EventViewSet, basename="collection-event")

note_router = routers.NestedSimpleRouter(case_router, "case", lookup="case")
note_router.register("note", NoteViewSet, basename="collection-note")

letter_router = routers.NestedSimpleRouter(case_router, "case", lookup="case")
letter_router.register("letter", LetterViewSet, basename="collection-letter")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(case_router.urls)),
    path("", include(event_router.urls)),
    path("", include(note_router.urls)),
    path("", include(letter_router.urls)),
]
