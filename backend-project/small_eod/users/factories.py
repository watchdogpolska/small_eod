import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence("user-{}".format)
    email = factory.LazyAttribute(lambda o: "%s@example.com" % o.username)
    password = factory.PostGenerationMethodCall("set_password", "pass")

    class Meta:
        model = User
        django_get_or_create = ("username",)
