from django.forms.models import model_to_dict
from rest_framework.views import APIView


class SendNotificationsMixin(APIView):
    notified_users = None
    ignored_fields = []
    init_instance = None

    def send_notifications(self, http_action, **kwargs):
        self.kwargs["pk"] = self.kwargs.get("pk", None) or kwargs["data"].get(
            "id", None
        )
        instance = None

        if http_action in ["post", "put"]:
            instance = self.get_object()
        else:
            instance = self.init_instance

        if http_action == "put" and not self.has_instance_changed(
            self.init_instance, instance
        ):
            return

        notified_users = self.get_notified_uers(instance)
        kwargs["actor"] = self.basename
        kwargs["action"] = self.action
        kwargs["instance"] = model_to_dict(instance)

        for user in notified_users:
            user.notify(**kwargs)

    def has_instance_changed(self, init_instance, instance):
        d1 = model_to_dict(init_instance)
        d2 = model_to_dict(instance)

        for field in self.ignored_fields:
            d1.pop(field, None)
            d2.pop(field, None)

        return d1 != d2

    def get_notified_uers(self, instance):
        if not self.notified_users:
            raise TypeError(
                "{} is missing a `notified_users` attribute.".format(
                    self.__class__.__name__
                )
            )
        for attr in self.notified_users.split("."):
            instance = getattr(instance, attr)
        return instance.all()

    def initial(self, request, *args, **kwargs):
        if (self.lookup_url_kwarg or self.lookup_field) in self.kwargs:
            self.init_instance = self.get_object()
        return super().initial(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        http_action = list(self.action_map.keys())[
            list(self.action_map.values()).index(self.action)
        ]
        if http_action in ["delete", "post", "put"]:
            self.send_notifications(http_action, data=response.data)
        return response
