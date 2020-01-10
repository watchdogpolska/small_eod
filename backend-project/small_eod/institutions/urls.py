from rest_framework import routers

from .views import InstitutionViewSet

app_name = "small_eod.institutions"

router = routers.SimpleRouter()
router.register("", InstitutionViewSet)
urlpatterns = router.urls
