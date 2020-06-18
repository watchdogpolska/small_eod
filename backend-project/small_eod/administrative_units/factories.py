import factory

from teryt_tree.models import JednostkaAdministracyjna
from teryt_tree.factories import JednostkaAdministracyjnaFactory as OriginalFactory

class JednostkaAdministracyjnaFactory(OriginalFactory):
    class Meta:
        model = JednostkaAdministracyjna
        django_get_or_create = ("pk",)
