import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence("user-{}".format)
    email = factory.Faker("email", locale="PL")
    password = factory.PostGenerationMethodCall("set_password", "pass")

    class Meta:
        model = User
        django_get_or_create = ("username",)
