from django.test import TestCase

from ..factories import ChannelFactory
from ..models import Channel
from ...generic.tests.mixins import FactoryTestCaseMixin


class ChannelFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = ChannelFactory
    MODEL = Channel
