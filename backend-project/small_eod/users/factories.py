import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):

    email = factory.Faker("email", locale="PL")
    username = factory.Sequence("user-{}".format)
    password = factory.PostGenerationMethodCall("set_password", "pass")

    class Meta:
        model = User
        django_get_or_create = ("username",)


def _add_obj(obj, create, extracted, **kwargs):
    if 'case' in kwargs:
        return getattr(kwargs['case'], kwargs['user_type']).add(obj)



class UserWithCaseFactory(UserFactory):
    # hook = factory.PostGeneration(lambda obj, create, extracted, **kwargs: kwargs['case'].responsible_users.add(obj))

    hook = factory.PostGeneration(_add_obj)
