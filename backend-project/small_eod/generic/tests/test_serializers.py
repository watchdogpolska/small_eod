class ResourceSerializerMixin:
    serializer_class = None
    factory_class = None

    def get_serializer_context(self):
        return {}

    def test_should_serialize_successfully(self):
        self.serializer_class(self.factory_class()).data

    def test_have_id_field(self):
        """
        All serializers of resource MUST have "id" field for management purpose
        """
        self.assertIn("id", self.serializer_class(self.factory_class()).data)
