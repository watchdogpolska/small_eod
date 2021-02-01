from django.urls import include, path
from rest_framework_nested import routers

from .views import FeatureOptionViewSet, FeatureViewSet

router = routers.SimpleRouter()
router.register("features", FeatureViewSet)

featureoption_router = routers.NestedSimpleRouter(router, "features", lookup="feature")
featureoption_router.register(
    "featureoption", FeatureOptionViewSet, basename="feature-featureoption"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(featureoption_router.urls)),
]
