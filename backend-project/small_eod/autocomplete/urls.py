from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (
    AdministrativeUnitAutocompleteViewSet,
    CaseAutocompleteViewSet,
    ChannelAutocompleteViewSet,
    DocumentTypeAutocompleteViewSet,
    FeatureOptionAutocompleteViewSet,
    InstitutionAutocompleteViewSet,
    TagsAutocompleteViewSet,
    UserAutocompleteViewSet,
)

router = SimpleRouter()
router.register("administrativeUnits", AdministrativeUnitAutocompleteViewSet)
router.register("cases", CaseAutocompleteViewSet)
router.register("channels", ChannelAutocompleteViewSet)
router.register("documentTypes", DocumentTypeAutocompleteViewSet)
router.register("features", FeatureOptionAutocompleteViewSet)
router.register("featureOptions", FeatureOptionAutocompleteViewSet)
router.register("institutions", InstitutionAutocompleteViewSet)
router.register("tags", TagsAutocompleteViewSet)
router.register("users", UserAutocompleteViewSet)

urlpatterns = [
    path("autocomplete/", include(router.urls)),
]
