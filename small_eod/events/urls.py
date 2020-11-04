from django.urls import path

from . import views

urlpatterns = [
    path("api/events/api", views.ical, name="event-ical-list"),
]
