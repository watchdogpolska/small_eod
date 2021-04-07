from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    AdministrativeUnitAutocompleteViewSet,
    CaseAutocompleteViewSet,
    ChannelAutocompleteViewSet,
    DocumentTypeAutocompleteViewSet,
    EventAutocompleteViewSet,
    FeatureOptionAutocompleteViewSet,
    InstitutionAutocompleteViewSet,
    LetterAutocompleteViewSet,
    NoteAutocompleteViewSet,
    TagAutocompleteViewSet,
    UserAutocompleteViewSet,
)

router = SimpleRouter()
router.register("administrativeUnits", AdministrativeUnitAutocompleteViewSet)
router.register("cases", CaseAutocompleteViewSet)
router.register("channels", ChannelAutocompleteViewSet)
router.register("documentTypes", DocumentTypeAutocompleteViewSet)
router.register("event", EventAutocompleteViewSet)
router.register("features", FeatureOptionAutocompleteViewSet)
router.register("featureOptions", FeatureOptionAutocompleteViewSet)
router.register("institutions", InstitutionAutocompleteViewSet)
router.register("letters", LetterAutocompleteViewSet)
router.register("notes", NoteAutocompleteViewSet)
router.register("tags", TagAutocompleteViewSet)
router.register("users", UserAutocompleteViewSet)

urlpatterns = [
    path("autocomplete/", include(router.urls)),
]
