from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    AdministrativeUnitAutocompleteViewSet,
    CaseAutocompleteViewSet,
    ChannelAutocompleteViewSet,
    DocumentTypeAutocompleteViewSet,
    ReferenceNumberAutocompleteViewSet,
    EventAutocompleteViewSet,
    FeatureAutocompleteViewSet,
    FeatureOptionAutocompleteViewSet,
    InstitutionAutocompleteViewSet,
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
router.register(
    "reference_numbers",
    ReferenceNumberAutocompleteViewSet,
    "autocomplete_reference_number",
)
router.register("events", EventAutocompleteViewSet, "autocomplete_event")
router.register("features", FeatureAutocompleteViewSet, "autocomplete_feature")
router.register(
    "feature_options", FeatureOptionAutocompleteViewSet, "autocomplete_feature_option"
)
router.register(
    "institutions", InstitutionAutocompleteViewSet, "autocomplete_institution"
)
router.register("tags", TagAutocompleteViewSet, "autocomplete_tag")
router.register("users", UserAutocompleteViewSet, "autocomplete_user")

urlpatterns = [
    path("autocomplete/", include(router.urls)),
]
