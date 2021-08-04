from django.forms.models import model_to_dict
from rest_framework.views import APIView


class NotificationsView(APIView):
    notified_users_field = None
    notification_diff_ignored_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._http_action = None
        self._init_instance = None

    def send_notifications(self, request, **kwargs):
        self.kwargs["pk"] = self.kwargs.get("pk", None) or kwargs["data"].get(
            "id", None
        )

        instance = (
            self.get_object()
            if self._http_action in ["post", "put", "patch"]
            else self._init_instance
        )

        if self._http_action == "put" and not self.has_instance_changed(
            self._init_instance, instance
        ):
            return

        notified_users = self.get_notified_uers(instance)
        kwargs["source"] = self.basename
        kwargs["action"] = self.action
        kwargs["instance"] = instance
        kwargs["request"] = request

        for user in notified_users:
            user.notify(**kwargs)

    def has_instance_changed(self, init_instance, instance):
        d1 = model_to_dict(init_instance)
        d2 = model_to_dict(instance)

        for field in self.notification_diff_ignored_fields:
            d1.pop(field, None)
            d2.pop(field, None)

        return d1 != d2

    def get_notified_uers(self, instance):
        if not self.notified_users_field:
            raise TypeError(
                "{} is missing a `notified_users_field` attribute.".format(
                    self.__class__.__name__
                )
            )

        for attr in self.notified_users_field.split("."):
            instance = getattr(instance, attr, None)

        if not instance:
            return []

        return instance.all()

    def initial(self, request, *args, **kwargs):
        self._http_action = next(
            k for k, v in self.action_map.items() if v == self.action
        )
        if self._http_action in ["put", "delete", "patch"]:
            self._init_instance = self.get_object()
        return super().initial(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        if self._http_action in ["delete", "post", "put", "patch"]:
            self.send_notifications(request=request, data=response.data)
        return response
