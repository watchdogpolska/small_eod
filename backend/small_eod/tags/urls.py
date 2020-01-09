from rest_framework import routers
from django.urls import path, include

from ..users.views import UserViewSet
from ..institutions.views import AddressDataViewSet, InstitutionViewSet
from ..cases.views import CaseViewSet
from ..dictionaries.views import DictionaryViewSet
from .views import TagViewSet
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('address', AddressDataViewSet)
router.register('institution', InstitutionViewSet)
router.register('case', CaseViewSet)
router.register('', TagViewSet)

app_name = 'tags'
urlpatterns = [
    path('', include(router.urls)),
]
