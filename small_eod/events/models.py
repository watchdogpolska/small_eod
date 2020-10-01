from typing import Optional

from django.core.mail import send_mail
from django.db import models
from django.forms.models import model_to_dict

from .apps import EventsSettings


class EventType(models.Model):
    name = models.CharField(
        unique=True,
        max_length=254
    )


class CaseEvent(models.Model):
    date = models.DateTimeField()

    event_type = models.ForeignKey(
        'events.EventType',
        on_delete=models.PROTECT
    )
    # if people are notified, this should be 'true'
    notified = models.BooleanField(
        default=False
    )
    name = models.CharField(
        unique=True,
        max_length=254
    )
    case = models.ForeignKey(
        'cases.Case',
        on_delete=models.PROTECT
    )
    subject = models.CharField(
        max_length=254,
        default='{event_type_name} - {name}'
    )
    message = models.TextField(
        max_length=254,
        default='{name}'
    )

    @property
    def email_format(self) -> dict:
        d = model_to_dict(self.case)
        d.setdefault('event_type_name', self.event_type.name)
        return d

    @property
    def notification_emails(self) -> Optional[list]:
        return [p.user.email for p in self.case.responsible_people.all() if getattr(p.user, 'email', None)]

    def email_users(self, subject=None, message=None) -> Optional[send_mail]:
        """
        If subject / message contains key not available in
        `self.email.format` - exception will be thrown.
        """
        if self.notification_emails:
            return send_mail(
                subject=subject or self.subject.format(**self.email_format),
                message=message or self.message.format(**self.email_format),
                from_email=EventsSettings.FROM_EMAIL,
                recipient_list=self.notification_emails,
                fail_silently=False
            )
