from typing import Type

from django.core.validators import ValidationError
from django.db.models import Model
from django.test import TestCase
from django.test import tag
from django.urls import reverse
from factory.django import DjangoModelFactory

from .validators import ExactLengthsValidator
from ..users.factories import UserFactory


class ReadOnlyViewSetMixin:
    basename = None
    serializer_class = None
    factory_class = None

    def setUp(self):
        if not self.factory_class:
            raise NotImplementedError("factory_class must be defined")
        self.obj = self.factory_class()
        self.user = getattr(self, "user", UserFactory(username="john"))
        self.client.login(username="john", password="pass")
        self.response_results_key = "results"

    def get_extra_kwargs(self):
        return dict()

    def get_url(self, name, **kwargs):
        if not self.basename:
            raise NotImplementedError("get_url must be overridden or basename defined")
        return reverse("{}-{}".format(self.basename, name), kwargs=kwargs)

    def test_dict_plain(self):
        parsed_response_len = 4
        response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
        parsed_response = response.json()
        response_result = parsed_response.get(self.response_results_key)

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response_result)
        self.assertEqual(len(parsed_response), parsed_response_len)
        self.validate_item(response_result[0])

    # def test_list_plain(self):
    #     response = self.client.get(self.get_url(name="list", **self.get_extra_kwargs()))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(len(response.json()), 1)
    #     self.validate_item(response.json()[0])

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


class FactoryCreateObjectsMixin:
    FACTORY = Type[DjangoModelFactory]
    MODEL = Type[Model]

    FACTORY_COUNT = 2

    @classmethod
    def create_factory(cls):
        return cls.FACTORY()

    def _test_factory_object(self, msg, count):
        obj = self.create_factory()
        self.assertEqual(
            count,
            self.MODEL.objects.all().count(),
            msg=f"Failed {msg} factory test - "
            f"position: {count} "
            f"model: {self.MODEL} "
            f"factory: {self.FACTORY} "
            f"object: {obj}",
        )

    @tag("FactoryCreateObjectsMixin")
    def test_factories_simple(self):
        self._test_factory_object(msg="simple", count=1)

    @tag("FactoryCreateObjectsMixin")
    def test_factories_many(self):
        for x in range(1, self.FACTORY_COUNT):
            self._test_factory_object(msg="many", count=x)

    # def test_print_to_console(self):
    #     """
    #     Show in the console how the data looks like.
    #     Just making sure that frontend has the right data
    #     to work with.
    #     """
    #     from django.forms import model_to_dict
    #     print(f"\n{model_to_dict(self.create_factory())}")


class ExactLengthsValidatorTestCase(TestCase):
    def test_validator_message(self):
        """
        Validator returns corrrect error message.
        """
        validator = ExactLengthsValidator([10, 14, 566, 1])

        with self.assertRaises(ValidationError) as err:
            validator("12")

        self.assertIn(
            "Ensure this value has length of any [10, 14, 566, 1] (it has 2).",
            err.exception,
        )

    def test_validator_values(self):
        """
        Given invalid values, validator raises `ValidationError`.
        Given valid values, validator does not raise `ValidationError`.
        """
        validator = ExactLengthsValidator([10, 14])

        # valid values
        chars_10 = "1111111111"
        self.assertEqual(len(chars_10), 10)
        chars_14 = "11111111111111"
        self.assertEqual(len(chars_14), 14)

        # invalid values
        chars_9 = "111111111"
        self.assertEqual(len(chars_9), 9)
        chars_12 = "111111111111"
        self.assertEqual(len(chars_12), 12)
        chars_15 = "111111111111111"
        self.assertEqual(len(chars_15), 15)

        # valid test
        validator(chars_10)
        validator(chars_14)

        # invalid test
        with self.assertRaises(ValidationError):
            validator(chars_9)

        with self.assertRaises(ValidationError):
            validator(chars_12)

        with self.assertRaises(ValidationError):
            validator(chars_15)
