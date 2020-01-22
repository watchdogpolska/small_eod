from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class UserLogModelSerializer(ModelSerializer):
    created_by = PrimaryKeyRelatedField(read_only=True)
    modified_by = PrimaryKeyRelatedField(read_only=True)

    def create(self, validated_data):
        instance = super().create(validated_data)

        current_user = self.context["request"].user
        instance.created_by = current_user
        instance.modified_by = current_user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().create(validated_data)

        current_user = self.context["request"].user
        instance.modified_by = current_user
        instance.save()
        return instance
