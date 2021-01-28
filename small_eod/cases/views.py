from icalendar import Calendar, Event as IEvent
from django.urls import reverse
from django.template import loader
from django.http import HttpResponse
from .models import Letter
from django.http import HttpResponseForbidden
from ..authkey.parser import get_token
from ..authkey.models import Key

calendar_description_template = "cases/letter/calendar_description.txt"


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
    cal.add("prodid", f"-//small-eod//letters//{key.user}//")
    cal.add("version", "2.0")
    for obj in Letter.objects.filter(event__isnull=True).select_related(
        "case", "case__audited_institution"
    ):
        letter = IEvent()
        url = request.build_absolute_uri(
            reverse("admin:cases_letter_change", kwargs={"object_id": str(obj.pk)})
        )
        description = t.render({"obj": obj}, request)
        categories = [obj.case]
        if obj.case.audited_institution:
            categories.append(obj.case.audited_institution)
        letter.add("uid", url)
        letter.add("dtstart", obj.event)
        letter.add("dtstamp", obj.event)
        letter.add("summary", obj.name)
        letter.add("created", obj.created_on)
        letter.add("last-modified", obj.modified_on)
        letter.add("url", url)
        letter.add("description", description)
        letter.add("categories", categories)
        cal.add_component(letter)
    return HttpResponse(content=cal.to_ical(), content_type="text/calendar")
