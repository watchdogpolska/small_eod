from django.urls import reverse

from ...users.mixins import AuthenticatedMixin


class ReadOnlyViewSetMixin(AuthenticatedMixin):
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

    def get_extra_kwargs(self):
        return dict()

    def get_url(self, name, **kwargs):
        if not self.basename:
            raise NotImplementedError("get_url must be overridden or basename defined")
        return reverse("{}-{}".format(self.basename, name), kwargs=kwargs)

    def get_url_list(self):
        return self.get_url(name="list", **self.get_extra_kwargs())

    def test_list_plain(self):
        self.login_required()
        response = self.client.get(self.get_url_list())
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

    def get_url_detail(self):
        return self.get_url(name="detail", **self.get_extra_kwargs(), pk=self.obj.pk)

    def test_retrieve_plain(self):
        self.login_required()
        response = self.client.get(
            self.get_url_detail()
        )
        self.assertEqual(response.status_code, 200)
        self.validate_item(response.json())

    def validate_item(self, item):
        raise NotImplementedError("validate_item must be overridden")


class UpdateViewSetMixin:
    def get_update_data(self):
        if not hasattr(self.obj, "name") and not self.serializer_class:
            raise NotImplementedError(
                "get_update_data must be overridden, because no 'name' field"
            )
        return {"name": f"{self.obj.name}-updated"}

    def validate_update_item(self, item):
        if not self.obj.name and not self.serializer_class:
            raise NotImplementedError(
                "validate_update_item must be defined, because no 'name' field"
            )
        self.assertEqual(item["id"], self.obj.pk)
        self.assertEqual(item["name"], f"{self.obj.name}-updated")

    def test_update_partial_plain(self):
        self.login_required()
        response = self.client.patch(
            self.get_url(name="detail", pk=self.obj.pk, **self.get_extra_kwargs()),
            data=self.get_update_data(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200, response.json())
        item = response.json()
        self.validate_update_item(item)


class GenericViewSetMixin(UpdateViewSetMixin, ReadOnlyViewSetMixin):
    def get_ommited_fields(self):
        if hasattr(self.serializer_class.Meta, "read_only_fields"):
            return self.serializer_class.Meta.read_only_fields + ["id"]
        else:
            return ["id"]

    def test_create_plain(self):
        self.login_required()
        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data=self.get_create_data(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201, response.json())
        item = response.json()
        self.assertNotEqual(item["id"], self.obj.pk)
        self.validate_item(item)

    def get_create_data(self):
        if not self.serializer_class:
            raise NotImplementedError("serializer_class must be defined")

        data = {
            key: value
            for (key, value) in self.serializer_class(self.obj).data.items()
            if key not in self.get_ommited_fields()
        }
        return data


class AuthorshipViewSetMixin:
    def test_created_by(self):
        if not hasattr(self, "obj"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )
        if not hasattr(self, "get_create_data"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )

        self.login_required()
        if not hasattr(self, "user"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )

        response = self.client.post(
            self.get_url(name="list", **self.get_extra_kwargs()),
            data=self.get_create_data(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["createdBy"], self.user.id)
        self.assertEqual(response.json()["modifiedBy"], self.user.id)

    def test_modified_by(self):
        if not hasattr(self, "obj"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )
        if not hasattr(self, "get_create_data"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )

        self.login_required()
        if not hasattr(self, "user"):
            raise NotImplementedError(
                "Authorship mixin must be used alongside the GenericViewSetMixin"
            )

        response = self.client.put(
            self.get_url(name="detail", **self.get_extra_kwargs(), pk=self.obj.pk),
            data=self.get_create_data(),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.json()["createdBy"], self.user.id)
        self.assertEqual(response.json()["modifiedBy"], self.user.id)
