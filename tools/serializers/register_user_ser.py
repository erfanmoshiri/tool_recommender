from django.contrib.auth.models import User
from rest_framework.fields import ListField, IntegerField, CharField
from rest_framework.serializers import Serializer


class RegisterUserSer(Serializer):
    phone = CharField(max_length=32)
    password = CharField(max_length=64)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        return User.objects.create_user(validated_data['phone'], password=validated_data['password'])

