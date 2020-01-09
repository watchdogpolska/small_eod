from rest_framework import routers
from django.urls import path, include

from .views import TagViewSet
router = routers.SimpleRouter()

router.register('', TagViewSet)

app_name = 'tags'
urlpatterns = [
    path('', include(router.urls)),
]
