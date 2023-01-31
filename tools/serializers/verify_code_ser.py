from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import Serializer


class VerifyCodeSer(Serializer):
    code_id = IntegerField()
    code = CharField(max_length=4)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
