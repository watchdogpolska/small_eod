from django.urls import include, path
from rest_framework_nested import routers

from .views import FeatureOptionViewSet, FeatureViewSet

router = routers.SimpleRouter()
router.register("features", FeatureViewSet)
router.register("featureOptions", FeatureOptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
