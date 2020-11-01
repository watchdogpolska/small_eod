from icalendar import Calendar, Event as IEvent
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.translation import ugettext as _
from drf_yasg2.utils import swagger_auto_schema
from .models import Event
from .serializers import EventSerializer
from ..authkey.permissions import AuthKeyPermission
from ..authkey.authentication import AuthKeyAuthentication
from rest_framework import status


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = [
        "id",
        "case__name",
        "name",
        "date",
        "comment",
    ]
    calendar_description_template = "events/calendar_description.txt"
    required_scopes_map = {
        "Ical": ["export_ical"],
    }

    def get_authenticators(self):
        if self.name == "Ical":
            return [AuthKeyAuthentication()]
        return super().get_authenticators()

    def get_permissions(self):
        if self.name == "Ical":
            return [AuthKeyPermission()]
        return super().get_permissions()

    @swagger_auto_schema(
        method="get",
        responses={status.HTTP_200_OK: "Export of calendar as 'text/calendar'"},
    )
    @action(detail=False, methods=["get"])
    def ical(self, request):
        cal = Calendar()
        cal["summary"] = _("small-eod - events")
        t = loader.get_template(self.calendar_description_template)

        for obj in (
            self.get_queryset()
            .select_related("case")
            .prefetch_related("case__audited_institutions")
        ):
            event = IEvent()
            url = request.build_absolute_uri(
                reverse(
                    "admin:events_event_change", kwargs={"object_id": str(obj.case.pk)}
                )
            )
            description = t.render({"obj": obj}, request)
            categories = [obj.case] + list(obj.case.audited_institutions.all())
            event.add("uid", obj.pk)
            event.add("dtstart", obj.date)
            event.add("summary", obj.name)
            event.add("created", obj.created_on)
            event.add("last-mod", obj.modified_on)
            event.add("url", url)
            event.add("description", description)
            event.add("categories", categories)
            cal.add_component(event)
        return HttpResponse(content=cal.to_ical(), content_type="text/calendar")
