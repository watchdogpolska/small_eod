from django.test import TestCase

from .factories import ChannelFactory
from .models import Channel
from ..generic.tests import FactoryCreateObjectsMixin


class ChannelFactoryTestCase(FactoryCreateObjectsMixin, TestCase):
    FACTORY = ChannelFactory
    MODEL = Channel
