from django.forms.models import model_to_dict
from rest_framework.views import APIView


class SendNotificationsMixin(APIView):
    notified_users = ""
    initial_instance = None

    def send_notifications(self, http_action, **kwargs):
        instance = None

        if http_action in ["post", "put"]:
            self.kwargs["pk"] = kwargs["data"]["id"]
            instance = self.get_object()
        else:
            instance = self.initial_instance

        notified_users = self.get_user_list(instance)
        sender = self.basename

        for user in notified_users:
            user.notify(sender, self.action, **kwargs)

    def get_user_list(self, instance):
        for attr in self.notified_users.split("."):
            instance = getattr(instance, attr)
        return instance.all()

    def initial(self, request, *args, **kwargs):
        if (self.lookup_url_kwarg or self.lookup_field) in self.kwargs:
            self.initial_instance = self.get_object()
        return super().initial(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(
            request, *args, **kwargs
        )
        http_action = list(self.action_map.keys())[
            list(self.action_map.values()).index(self.action)
        ]
        if http_action in ["delete", "post", "put"]:
            self.send_notifications(http_action, data=response.data)
        return response

    """
    def get_changes(self, init_instance, instance):
        d1 = model_to_dict(init_instance)
        d2 = model_to_dict(instance)
        diff = dict([(k, (v, d2[k])) for k, v in d1.items() if v != d2[k]])

        changes = {}
        for field, field_changes in diff.items():
            before, after = field_changes[0], field_changes[1]
            if type(before) == list:
                removed, added = self._remove_common(before, after)
                changes.update({field: {"added": added, "removed": removed, "changed": None}})
            else:
                changes.update({field: {"added": None, "removed": None, "changed": {"from": before, "to": after}}})

        return changes

    def _remove_common(self, l1, l2):
        for element in l1.copy() if len(l1) > len(l2) else l2.copy():
            if element in l1 and element in l2:
                l1.remove(element)
                l2.remove(element)
        return l1, l2
    """
