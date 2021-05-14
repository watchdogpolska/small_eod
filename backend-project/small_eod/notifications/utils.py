import logging
import random
import sys
from enum import Enum

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
    CASE_CREATE = auto()
    CASE_UPDATE = auto()
    CASE_DESTROY = auto()


class MailTemplate:
    def __init__(self, txt_path, html_path=None):
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
        TemplateKey.CASE_DESTROY: [MailTemplate.from_prefix("cases/email/case_closed")],
        TemplateKey.CASE_UPDATE: [MailTemplate.from_prefix("cases/email/case_updated")],
    }

    @classmethod
    def send(cls, template_key, recipient_list, context=None, from_email=None, **kwds):
        template = random.choice(cls.TEMPLATE_MAP[template_key])
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
