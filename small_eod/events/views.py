from icalendar import Calendar, Event as IEvent
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse
from .models import Event
from django.http import HttpResponseForbidden
from ..authkey.parser import get_token
from ..authkey.models import Key

calendar_description_template = "events/calendar_description.txt"


def ical(request):
    t = loader.get_template(calendar_description_template)

    token = get_token(request)
    if not token:
        return HttpResponseForbidden("Missing authentication token")
    try:
        key = Key.objects.select_related("user").get(token=token)
    except Key.DoesNotExist:
        return HttpResponseForbidden("Invalid authentication token")
    if not key.has_scopes(["export_ical"]):
        return HttpResponseForbidden("Unauthorized operation for the token")
    key.update_used_on()

    cal = Calendar()
    cal.add("prodid", f"-//small-eod//events//{key.user}//")
    cal.add("version", "2.0")
    for obj in Event.objects.select_related("case", "case__audited_institution"):
        event = IEvent()
        url = request.build_absolute_uri(
            reverse("admin:events_event_change", kwargs={"object_id": str(obj.case.pk)})
        )
        description = t.render({"obj": obj}, request)
        categories = [obj.case]
        if obj.case.audited_institution:
            categories.append(obj.case.audited_institution)
        event.add("uid", url)
        event.add("dtstart", obj.date)
        event.add("dtstamp", obj.date)
        event.add("summary", obj.name)
        event.add("created", obj.created_on)
        event.add("last-modified", obj.modified_on)
        event.add("url", url)
        event.add("description", description)
        event.add("categories", categories)
        cal.add_component(event)
    return HttpResponse(content=cal.to_ical(), content_type="text/calendar")
