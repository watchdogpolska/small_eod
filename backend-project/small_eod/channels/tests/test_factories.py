from django.test import TestCase

from ...generic.tests.mixins import FactoryTestCaseMixin
from ..factories import ChannelFactory
from ..models import Channel


class ChannelFactoryTestCase(FactoryTestCaseMixin, TestCase):
    FACTORY = ChannelFactory
    MODEL = Channel
