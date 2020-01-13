from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField


class UserLogModelSerializer(ModelSerializer):
    created_by = PrimaryKeyRelatedField(read_only=True)
    modified_by = PrimaryKeyRelatedField(read_only=True)

    def get_current_user(self):
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            return request.user
        return None

    def create(self, validated_data):
        instance = super().create(validated_data)

        current_user = self.get_current_user()
        instance.created_by = current_user
        instance.modified_by = current_user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().create(validated_data)

        current_user = self.get_current_user()
        instance.modified_by = current_user
        instance.save()
        return instance
