from django.urls import path

from . import views

urlpatterns = [
    path("api/letters/api", views.ical, name="letter-ical-list"),
]
