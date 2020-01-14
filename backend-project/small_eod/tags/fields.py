from rest_framework import serializers


class TagField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return [
            self.child.to_representation(item) if item is not None else None
            for item in data.all()
        ]
