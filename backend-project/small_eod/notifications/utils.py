import sys
from enum import Enum

import logging
from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives
from django.template import loader

logger = logging.getLogger(__name__)


def make_auto():
    """eum.auto replacement"""

    def loop():
        i = 1
        while True:
            yield i
            i += 1

    loop = loop()
    return lambda: next(loop)


auto = make_auto()


class TemplateKey(Enum):
    CASE_CLOSED = auto()
    CASE_GRANT_GROUP = auto()
    CASE_GRANTED = auto()
    CASE_NEW = auto()
    CASE_REGISTERED = auto()
    CASE_UPDATED = auto()

    EVENT_CREATED = auto()
    EVENT_UPDATED = auto()
    EVENT_REMINDER = auto()

    LETTER_ACCEPTED = auto()
    LETTER_CREATED = auto()
    LETTER_DROP_A_NOTE = auto()
    LETTER_SEND_TO_CLIENT = auto()
    LETTER_UPDATED = auto()

    USER_NEW = auto()

    @classmethod
    def get_by_target_verb(cls, target, verb):
        model_name = target._meta.model_name
        name = "{model}_{verb}".format(model=model_name, verb=verb).upper()
        return TemplateKey[name]


class MailTemplate:
    def __init__(self, txt_path, html_path=None):
        self.txt_path = txt_path
        self.html_path = html_path

    def __str__(self):
        return "{}-{}".format(self.txt_path, self.html_path)

    @classmethod
    def from_prefix(cls, prefix):
        txt_path = prefix + ".txt"
        html_path = prefix + ".html"
        return cls(txt_path, html_path)

    def render(self, context):
        txt = loader.get_template(self.txt_path).render(context)
        html = loader.get_template(self.html_path).render(context)
        return (txt, html)


class TemplateMailManager:

    TEMPLATE_MAP = {
        TemplateKey.CASE_CLOSED: MailTemplate.from_prefix("cases/email/case_closed"),
        TemplateKey.CASE_GRANT_GROUP: MailTemplate.from_prefix(
            "cases/email/case_grant_group"
        ),
        TemplateKey.CASE_GRANTED: MailTemplate.from_prefix("cases/email/case_granted"),
        TemplateKey.CASE_NEW: MailTemplate.from_prefix("cases/email/case_new"),
        TemplateKey.CASE_REGISTERED: MailTemplate.from_prefix(
            "cases/email/case_registered"
        ),
        TemplateKey.CASE_UPDATED: MailTemplate.from_prefix("cases/email/case_updated"),
        TemplateKey.EVENT_CREATED: MailTemplate.from_prefix(
            "events/email/event_created"
        ),
        TemplateKey.EVENT_UPDATED: MailTemplate.from_prefix(
            "events/email/event_updated"
        ),
        TemplateKey.EVENT_REMINDER: MailTemplate.from_prefix(
            "events/email/event_reminder"
        ),
        TemplateKey.LETTER_ACCEPTED: MailTemplate.from_prefix(
            "letters/email/letter_accepted"
        ),
        TemplateKey.LETTER_CREATED: MailTemplate.from_prefix(
            "letters/email/letter_created"
        ),
        TemplateKey.LETTER_DROP_A_NOTE: MailTemplate.from_prefix(
            "letters/email/letter_drop_a_note"
        ),
        TemplateKey.LETTER_SEND_TO_CLIENT: MailTemplate.from_prefix(
            "letters/email/letter_send_to_client"
        ),
        TemplateKey.LETTER_UPDATED: MailTemplate.from_prefix(
            "letters/email/letter_updated"
        ),
        TemplateKey.USER_NEW: MailTemplate.from_prefix("users/email/new_user"),
    }

    @classmethod
    def send(cls, template_key, recipient_list, context=None, from_email=None, **kwds):
        template = cls.TEMPLATE_MAP[template_key]
        txt, html = template.render(context or {})
        subject, txt = txt.strip().split("\n", 1)
        from_email = from_email if from_email else settings.DEFAULT_FROM_EMAIL
        headers = {}
        if len(sys.argv) > 1 and sys.argv[1] == "test":
            headers["Template"] = str(template)
        return cls._send_mail_with_header(
            subject=subject.strip(),
            message=txt,
            html_message=html,
            from_email=from_email,
            recipient_list=recipient_list,
            headers=headers,
            **kwds,
        )

    @staticmethod
    def _send_mail_with_header(
        subject,
        message,
        from_email,
        recipient_list,
        fail_silently=False,
        auth_user=None,
        auth_password=None,
        connection=None,
        html_message=None,
        headers=None,
    ):
        """
        Fork of django.core.mail.send_mail to add haders attribute
        """
        connection = connection or get_connection(
            username=auth_user, password=auth_password, fail_silently=fail_silently
        )
        mail = EmailMultiAlternatives(
            subject,
            message,
            from_email,
            recipient_list,
            connection=connection,
            headers=headers or {},
        )
        if html_message:
            mail.attach_alternative(html_message, "text/html")
        return mail.send()