from rest_framework.fields import ListField, IntegerField
from rest_framework.serializers import Serializer


class TooPerfSerializer(Serializer):
    features = ListField(
        child=IntegerField()
    )

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
