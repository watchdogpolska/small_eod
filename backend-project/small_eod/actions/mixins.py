from rest_framework import mixins


class Actions:
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    DESTROY = "DESTROY"


class ActionException(Exception):
    """
    Pushing message failed!
    """


class DummyPusher:
    def __init__(self):
        self.queue = []

    def __call__(self, serializer, action):
        self.queue.append(dict(serializer=serializer, action=action))


dummy_pusher, dummy_pusher2 = DummyPusher(), DummyPusher()


class ActionMixin:

    action_handlers = [dummy_pusher, dummy_pusher2]

    def handle_actions(self, serializer, action):
        for handle in self.action_handlers:
            try:
                handle(serializer, action)
            except ActionException as exc:
                print("Ups...", exc)


class MQCreateModelMixin(mixins.CreateModelMixin):
    def perform_create(self, serializer):
        super().perform_create(serializer)

        self.handle_actions(
            serializer=serializer, action=Actions.CREATE,
        )


class MQUpdateModelMixin(mixins.UpdateModelMixin):
    def perform_update(self, serializer):
        super().perform_update(serializer)

        self.handle_actions(
            serializer=serializer, action=Actions.UPDATE,
        )


class MQDestroyModelMixin(mixins.DestroyModelMixin):
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

        self.handle_actions(
            serializer=self.get_serializer(instance=instance), action=Actions.DESTROY,
        )
