from django.test import TestCase

from ..factories import ChannelFactory
from ..models import Channel
from ...generic.tests.factories import FactoryTestCaseMixin


class ChannelFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = ChannelFactory
    MODEL = Channel
