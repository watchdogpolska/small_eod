from rest_framework import routers

from .views import InstitutionViewSet

app_name = 'institutions'

router = routers.SimpleRouter()
router.register('', InstitutionViewSet)
urlpatterns = router.urls
