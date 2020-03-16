from rest_framework_nested import routers
from .views import (
    FeatureViewSet,
    FeatureOptionViewSet,
)

from django.urls import path, include

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
