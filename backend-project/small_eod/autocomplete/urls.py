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
router.register(
    "administrative_units",
    AdministrativeUnitAutocompleteViewSet,
    "autocomplete_administrative_unit",
)
router.register("cases", CaseAutocompleteViewSet, "autocomplete_case")
router.register("channels", ChannelAutocompleteViewSet, "autocomplete_channel")
router.register(
    "document_types", DocumentTypeAutocompleteViewSet, "autocomplete_document_type"
)
router.register("events", EventAutocompleteViewSet, "autocomplete_event")
router.register("features", FeatureOptionAutocompleteViewSet, "autocomplete_feature")
router.register(
    "feature_options", FeatureOptionAutocompleteViewSet, "autocomplete_feature_option"
)
router.register(
    "institutions", InstitutionAutocompleteViewSet, "autocomplete_institution"
)
router.register("letters", LetterAutocompleteViewSet, "autocomplete_letter")
router.register("notes", NoteAutocompleteViewSet, "autocomplete_note")
router.register("tags", TagAutocompleteViewSet, "autocomplete_tag")
router.register("users", UserAutocompleteViewSet, "autocomplete_user")

urlpatterns = [
    path("autocomplete/", include(router.urls)),
]
