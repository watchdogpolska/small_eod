from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import JednostkaAdministracyjnaViewSet

router = SimpleRouter()
router.register(
    "administrative_units",
    JednostkaAdministracyjnaViewSet,
    basename="administrative_unit",
)

urlpatterns = [
    path("", include(router.urls)),
]
