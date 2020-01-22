from django.core.exceptions import ValidationError
from teryt_tree.models import JednostkaAdministracyjna
from django.utils.translation import ugettext_lazy as _


def validate_level_3(administrative_unit):
    administrative_unit_object = JednostkaAdministracyjna.objects.get(pk=administrative_unit)
    if administrative_unit_object.category.level != 3:
        raise ValidationError(_("Must be level 3 administrative unit."))
