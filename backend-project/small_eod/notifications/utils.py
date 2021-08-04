import logging
import random
from enum import Enum, auto

from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.template import loader

logger = logging.getLogger(__name__)


class TemplateKey(Enum):
    CASE_CREATE = auto()
    CASE_UPDATE = auto()
    CASE_PARTIAL_UPDATE = CASE_UPDATE
    CASE_DESTROY = auto()
    EVENT_CREATE = auto()
    EVENT_UPDATE = auto()
    EVENT_PARTIAL_UPDATE = EVENT_UPDATE
    EVENT_DESTROY = auto()
    NOTE_CREATE = auto()
    NOTE_UPDATE = auto()
    NOTE_PARTIAL_UPDATE = NOTE_UPDATE
    NOTE_DESTROY = auto()
    LETTER_CREATE = auto()
    LETTER_UPDATE = auto()
    LETTER_PARTIAL_UPDATE = LETTER_UPDATE
    LETTER_DESTROY = auto()
    NOTIFICATION_TEST = auto()


class MailTemplate:
    def __init__(self, txt_path, html_path):
        self.txt_path = txt_path
        self.html_path = html_path

    def __str__(self):
        return f"{self.txt_path}-{self.html_path}"

    @classmethod
    def from_prefix(cls, prefix):
        txt_path = prefix + ".txt"
        html_path = prefix + ".html"
        return cls(txt_path, html_path)

    def render(self, context):
        txt = loader.get_template(self.txt_path).render(context)
        html = loader.get_template(self.html_path).render(context)
        return txt, html


class TemplateMailManager:
    TEMPLATE_MAP = {
        TemplateKey.CASE_CREATE: [MailTemplate.from_prefix("cases/email/case_created")],
        TemplateKey.CASE_DESTROY: [
            MailTemplate.from_prefix("cases/email/case_removed")
        ],
        TemplateKey.CASE_UPDATE: [MailTemplate.from_prefix("cases/email/case_updated")],
        TemplateKey.CASE_PARTIAL_UPDATE: [
            MailTemplate.from_prefix("cases/email/case_updated")
        ],
        TemplateKey.EVENT_CREATE: [
            MailTemplate.from_prefix("events/email/event_created")
        ],
        TemplateKey.EVENT_PARTIAL_UPDATE: [
            MailTemplate.from_prefix("events/email/event_updated")
        ],
        TemplateKey.EVENT_UPDATE: [
            MailTemplate.from_prefix("events/email/event_updated")
        ],
        TemplateKey.EVENT_DESTROY: [
            MailTemplate.from_prefix("events/email/event_removed")
        ],
        TemplateKey.NOTE_CREATE: [MailTemplate.from_prefix("notes/email/note_created")],
        TemplateKey.NOTE_UPDATE: [MailTemplate.from_prefix("notes/email/note_updated")],
        TemplateKey.NOTE_PARTIAL_UPDATE: [
            MailTemplate.from_prefix("notes/email/note_updated")
        ],
        TemplateKey.NOTE_DESTROY: [
            MailTemplate.from_prefix("notes/email/note_removed")
        ],
        TemplateKey.LETTER_CREATE: [
            MailTemplate.from_prefix("letters/email/letter_created")
        ],
        TemplateKey.LETTER_UPDATE: [
            MailTemplate.from_prefix("letters/email/letter_updated")
        ],
        TemplateKey.LETTER_PARTIAL_UPDATE: [
            MailTemplate.from_prefix("letters/email/letter_updated")
        ],
        TemplateKey.LETTER_DESTROY: [
            MailTemplate.from_prefix("letters/email/letter_removed")
        ],
        TemplateKey.NOTIFICATION_TEST: [
            MailTemplate.from_prefix("notifications/email/test_notifications")
        ],
    }

    @classmethod
    def send(cls, template_key, recipient_list, context=None, from_email=None):
        template = random.choice(cls.TEMPLATE_MAP[template_key])
        txt, html = template.render(context or {})
        subject, txt = txt.strip().split("\n", 1)
        from_email = from_email if from_email else settings.DEFAULT_FROM_EMAIL
        headers = {"Action": context["action"]}
        mail = EmailMultiAlternatives(
            subject, txt, from_email, recipient_list, headers=headers
        )
        mail.attach_alternative(html, "text/html")

        return mail.send()
