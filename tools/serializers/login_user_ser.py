from django.contrib.auth.models import User
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class LoginUserSer(Serializer):
    phone = CharField(max_length=32)
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def exists(self):
        return User.objects.filter(username=self.validated_data['phone']).first()
