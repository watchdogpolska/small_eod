from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def notify(self, sender, action, **kwargs):
        pass

    def get_enabled_notifications(self):
        pass
