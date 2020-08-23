from rest_framework_nested import routers
from .views import (
    CollectionViewSet,
    CaseViewSet,
    EventViewSet,
    LetterViewSet,
    NoteViewSet,
    TokenCreateAPIView,
)

from django.urls import path, include

router = routers.SimpleRouter()
router.register("collections", CollectionViewSet)

case_router = routers.NestedSimpleRouter(router, "collections", lookup="collection")
case_router.register("cases", CaseViewSet, basename="collection-case")

event_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
event_router.register("events", EventViewSet, basename="collection-event")

note_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
note_router.register("notes", NoteViewSet, basename="collection-note")

letter_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
letter_router.register("letters", LetterViewSet, basename="collection-letter")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(case_router.urls)),
    path("", include(event_router.urls)),
    path("", include(note_router.urls)),
    path("", include(letter_router.urls)),
    path(
        "collections/<collection_pk>/tokens/",
        TokenCreateAPIView.as_view(),
        name="collection-tokens-list",
    ),
]
