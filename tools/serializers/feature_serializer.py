from rest_framework.fields import ListField, IntegerField, CharField
from rest_framework.serializers import ModelSerializer, Serializer

from tools.models import Feature


class FeatureSerializer(Serializer):
    id = IntegerField()
    name = CharField()

    class Meta:
        # model = Feature
        fields = ('id', 'name')
