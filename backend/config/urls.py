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
from netbox.views import APIRootView, HomeView, SearchView
from drf_yasg.views import get_schema_view
from .swagger import info

schema_view = get_schema_view(
    info,
    validators=['flex', 'ssv'],
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', APIRootView.as_view(), name='api-root'),
    path('api/institutions/', include('small_eod.institutions.urls')),

    path('api/docs/', schema_view.with_ui('swagger'), name='api_docs'),
    path('api/redoc/', schema_view.with_ui('redoc'), name='api_redocs'),
    re_path('^api/swagger(?P<format>.json|.yaml)$', schema_view.without_ui(), name='schema_swagger'),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
