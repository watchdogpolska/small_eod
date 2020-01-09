from rest_framework.serializers import ModelSerializer


class UserLogModelSerializer(ModelSerializer):

    def create(self, validated_data):
        instance = super().create(validated_data)

        current_user = self.context['request'].user
        instance.createdBy = current_user
        instance.modifiedBy = current_user
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance = super().create(validated_data)

        current_user = self.context['request'].user
        instance.modifiedBy = current_user
        instance.save()
        return instance
