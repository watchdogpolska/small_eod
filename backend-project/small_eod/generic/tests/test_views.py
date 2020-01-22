from django.urls import reverse

from ...users.factories import UserFactory


class ReadOnlyViewSetMixin:
    basename = None
    serializer_class = None
    factory_class = None

    paginated_response_results_key = "results"
    paginated = True
    parsed_response_len = 4

    def setUp(self):
        if not self.factory_class:
            raise NotImplementedError("factory_class must be defined")

        self.obj = self.factory_class()
        self.user = getattr(self, "user", UserFactory(username="john"))
        self.client.login(username="john", password="pass")

    def get_extra_kwargs(self):
        return dict()

    def get_url(self, name, **kwargs):
        if not self.basename:
            raise NotImplementedError("get_url must be overridden or basename defined")
        return reverse("{}-{}".format(self.basename, name), kwargs=kwargs)

    def test_list_plain(self):
        response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        parsed_response = response.json()
        response_result = (
            parsed_response.get(self.paginated_response_results_key)
            if self.paginated is True
            else parsed_response
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(parsed_response), self.parsed_response_len)
        self.assertIs(type(response_result), list)
        self.validate_item(response_result[0])

    def test_retrieve_plain(self):
        response = self.client.get(
            self.get_url(name="detail", **self.get_extra_kwargs(), pk=self.obj.pk)
        )
        self.assertEqual(response.status_code, 200)
        self.validate_item(response.json())

    def validate_item(self, item):
        raise NotImplementedError("validate_item must be overridden")


class GenericViewSetMixin(ReadOnlyViewSetMixin):
    def get_ommited_fields(self):
        return self.serializer_class.Meta.read_only_fields

    def test_create_plain(self):
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data=self.get_create_data(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        item = response.json()
        self.assertNotEqual(item["id"], self.obj.pk)
        self.validate_item(item)

    def get_create_data(self):
        if not self.serializer_class:
            raise NotImplementedError("serializer_class must be defined")
        data = self.serializer_class(self.obj).data
        for field in self.get_ommited_fields():
            del data[field]
        del data["id"]
        return data
