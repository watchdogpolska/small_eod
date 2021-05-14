from django.contrib.auth.models import AbstractUser

from ..notifications.utils import TemplateKey, TemplateMailManager


class User(AbstractUser):
    def notify(self, actor, action, **kwargs):
        enabled = self.get_enabled_notifications()
        key = getattr(TemplateKey, f"{actor}_{action}".upper(), None)
        if key not in enabled:
            return False

        return TemplateMailManager.send(
            template_key=key, recipient_list=[self.email], context=kwargs
        )

    def get_enabled_notifications(self):
        return TemplateMailManager.TEMPLATE_MAP.keys()
