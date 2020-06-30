from teryt_tree.models import JednostkaAdministracyjna


class AdministrativeUnit(JednostkaAdministracyjna):
    class Meta:
        proxy = True
