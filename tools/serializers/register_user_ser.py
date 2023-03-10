from django.contrib.auth.models import User
from rest_framework.fields import CharField
from rest_framework.serializers import Serializer


class RegisterUserSer(Serializer):
    phone = CharField(max_length=32)
    full_name = CharField(max_length=64)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return User.objects.create_user(validated_data['phone'], first_name=validated_data['full_name'])

    def exists(self):
        return User.objects.filter(username=self.validated_data['phone']).exists()
