from rest_framework import serializers


class TagField(serializers.ListField):
    child = serializers.CharField()

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("default", [])
        kwargs.setdefault("min_length", 0)
        super().__init__(*args, **kwargs)

    def to_representation(self, data):
        return [
            self.child.to_representation(item) if item is not None and hasattr(item, 'all') else None
            for item in data.all()
        ]
