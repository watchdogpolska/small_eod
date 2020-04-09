from rest_framework_nested import routers
from .views import UserViewSet

from django.urls import path, include

router = routers.SimpleRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
