from django.test import TestCase
from .models import Case
from .serializers import CaseSerializer
from ..tags.models import Tag
from ..dictionaries.factories import FeatureFactory, DictionaryFactory

# Create your tests here.
class CaseSerializerTestCase(TestCase):
    def test_save_tag_value(self):
        serializer = CaseSerializer(data={
            "name": "Polska Fundacja Narodowa o rejestr umów",
            "auditedInstitution": [],
            "comment": "xxx",
            "responsibleUser": [],
            "notifiedUser": [],
            "feature": [],
            "tag": ["rejestr umów"],
        })
        self.assertTrue(serializer.is_valid(), serializer.errors)
        obj = serializer.save()
        self.assertTrue(Tag.objects.count(), 1)
        self.assertEqual(obj.tag.all()[0].name, "rejestr umów")
    
    def test_raise_for_over_maximum_feature(self):
        dictionary = DictionaryFactory(maxItems=3)
        features = FeatureFactory.create_batch(size=5, dictionary=dictionary)
        serializer = CaseSerializer(data={
            "name": "Polska Fundacja Narodowa o rejestr umów",
            "auditedInstitution": [],
            "comment": "xxx",
            "responsibleUser": [],
            "notifiedUser": [],
            "feature": [x.id for x in features],
            "tag": [],
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors.keys()), set(['feature']))
