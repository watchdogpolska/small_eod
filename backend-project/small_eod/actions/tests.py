from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.viewsets import GenericViewSet

from .mixins import ActionMixin, dummy_pusher2, dummy_pusher
from .mixins import MQCreateModelMixin, MQDestroyModelMixin, MQUpdateModelMixin
from ..channels.models import Channel
from ..channels.serializers import ChannelSerializer
from ..users.factories import UserFactory


class TestActionMixins(TestCase):
    class ChannelActionViewset(
        ActionMixin,
        MQCreateModelMixin,
        MQUpdateModelMixin,
        MQDestroyModelMixin,
        GenericViewSet,
    ):
        queryset = Channel.objects.all()
        serializer_class = ChannelSerializer

    def setUp(self) -> None:
        self.user = UserFactory()
        self.view = self.ChannelActionViewset.as_view(
            dict(post="create", delete="destroy", put="update")
        )

    def get_response(self, method, **kwargs):
        request = getattr(APIRequestFactory(), method)("/", **kwargs)
        force_authenticate(request, user=self.user)
        return request, self.view(request)

    def test_pushers_post(self):
        data = dict(name="test", postal_code=True)
        request, response = self.get_response("post", data=data)

        self.assertEqual(201, response.status_code, msg=response.data)
        self.assertEqual(1, len(dummy_pusher.queue))
        self.assertEqual(1, len(dummy_pusher2.queue))
        self.assertEqual(
            dummy_pusher.queue[0]["serializer"].data["name"], data["name"],
        )
