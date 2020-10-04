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
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from drf_yasg.views import get_schema_view
from .swagger import info
from small_eod.channels.views import ChannelViewSet
from small_eod.events.views import EventViewSet
from small_eod.institutions.views import InstitutionViewSet
from small_eod.notes.views import NoteViewSet
from small_eod.tags.views import TagViewSet
from small_eod.users.views import UserViewSet
from rest_framework import routers
from rest_framework import permissions
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r"channels", ChannelViewSet)
router.register(r"events", EventViewSet)
router.register(r"institutions", InstitutionViewSet)
router.register(r"notes", NoteViewSet)
router.register(r"tags", TagViewSet)
router.register(r"users", UserViewSet)

schema_view = get_schema_view(
    info,
    # validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("small_eod.collections.urls")),
    path("api/", include("small_eod.cases.urls")),
    path("api/", include("small_eod.letters.urls")),
    path("api/", include("small_eod.features.urls")),
    path("api/", include("small_eod.administrative_units.urls")),
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
