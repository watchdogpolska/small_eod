"""small_eod URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import re

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg2.views import get_schema_view
from rest_framework import permissions, routers

from small_eod.channels.views import ChannelViewSet
from small_eod.events.views import EventViewSet
from small_eod.institutions.views import InstitutionViewSet
from small_eod.notes.views import NoteViewSet
from small_eod.tags.views import TagViewSet
from small_eod.users.views import UserViewSet

from .swagger import info


class BetterDefaultRouter(routers.DefaultRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_urls = []
        self.api_root_dict = {}

    def get_urls(self):
        urls = super().get_urls()
        urls.extend(self.include_urls)
        return urls

    def include(self, module):
        urlpatterns = getattr(include(module)[0], "urlpatterns")
        viewnames = set()
        for urlpattern in urlpatterns:
            self.include_urls.append(urlpattern)
            if hasattr(urlpattern, "url_patterns"):
                viewnames.update([pattern.name for pattern in urlpattern.url_patterns])
            elif hasattr(urlpattern, "name"):
                viewnames.add(urlpattern.name)
        self.api_root_dict.update({
            re.sub(r"-list$", "", viewname): viewname for viewname in viewnames
        })

    def get_api_root_view(self, api_urls=None):
        api_root_dict = {}
        list_name = self.routes[0].name

        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = list_name.format(basename=basename)
        api_root_dict.update(self.api_root_dict)

        return self.APIRootView.as_view(api_root_dict=api_root_dict)


router = BetterDefaultRouter()

router.register(r"channels", ChannelViewSet)
router.register(r"events", EventViewSet)
router.register(r"institutions", InstitutionViewSet)
router.register(r"notes", NoteViewSet)
router.register(r"tags", TagViewSet)
router.register(r"users", UserViewSet)
router.include("small_eod.cases.urls")
router.include("small_eod.features.urls")
router.include("small_eod.collections.urls")
router.include("small_eod.letters.urls")
router.include("small_eod.administrative_units.urls")
router.include("small_eod.autocomplete.urls")

schema_view = get_schema_view(
    info,
    # validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/docs/", schema_view.with_ui("swagger"), name="api_docs"),
    path("api/redoc/", schema_view.with_ui("redoc"), name="api_redocs"),
    re_path(
        "^api/swagger(?P<format>.json|.yaml)$",
        schema_view.without_ui(),
        name="schema_swagger",
    ),
    path("api/", include(router.urls)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
