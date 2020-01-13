from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter
from rest_framework.routers import SimpleRouter

from .views import CaseViewSet, ResponsibleUserViewSet, NotifiedUserViewSet

router = SimpleRouter()
router.register('cases', CaseViewSet, basename='cases')

user_router = NestedSimpleRouter(router, 'cases', lookup='case')
user_router.register(
    'responsibleUser',
    ResponsibleUserViewSet,
    basename='cases-responsible_user'
)
user_router.register(
    r'notifiedUser',
    NotifiedUserViewSet,
    basename='cases-notified_user'
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(user_router.urls)),
]
