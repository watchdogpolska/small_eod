from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import SimpleRouter

from .views import CaseViewSet, ResponsibleUserViewSet, NotifiedUserViewSet

router = SimpleRouter()
router.register("cases", CaseViewSet, basename="case")

user_router = NestedSimpleRouter(router, "cases", lookup="case")
user_router.register(
    "responsibleUsers", ResponsibleUserViewSet, basename="case-responsible_user"
)
user_router.register(
    "notifiedUsers", NotifiedUserViewSet, basename="case-notified_user"
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_router.urls)),
]
