from rest_framework import routers

from .views import InstitutionViewSet


router = routers.SimpleRouter()
router.register('', InstitutionViewSet)
urlpatterns = router.urls
