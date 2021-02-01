from django.urls import include, path
from rest_framework_nested import routers

from .views import (
    CaseCollectionViewSet,
    CollectionViewSet,
    EventCollectionViewSet,
    LetterCollectionViewSet,
    NoteCollectionViewSet,
    TokenCreateAPIView,
)

router = routers.SimpleRouter()
router.register("collections", CollectionViewSet)

case_router = routers.NestedSimpleRouter(router, "collections", lookup="collection")
case_router.register("cases", CaseCollectionViewSet, basename="collection-case")

event_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
event_router.register("events", EventCollectionViewSet, basename="collection-event")

note_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
note_router.register("notes", NoteCollectionViewSet, basename="collection-note")

letter_router = routers.NestedSimpleRouter(case_router, "cases", lookup="case")
letter_router.register("letters", LetterCollectionViewSet, basename="collection-letter")

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
