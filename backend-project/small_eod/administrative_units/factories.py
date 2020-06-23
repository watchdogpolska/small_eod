from teryt_tree.factories import JednostkaAdministracyjnaFactory as OriginalFactory
import factory
import factory.fuzzy


class JednostkaAdministracyjnaFactory(OriginalFactory):
    # TODO: Move changes upstream
    pk = factory.fuzzy.FuzzyText(length=7)
