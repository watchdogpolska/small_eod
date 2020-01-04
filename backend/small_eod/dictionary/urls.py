from api.urls import router

from dictionary.views import DictionaryViewSet

router.register('dictionary', DictionaryViewSet)


