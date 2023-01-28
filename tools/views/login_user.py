from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.serializers import RegisterUserSer


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ser = RegisterUserSer(data=request.data)
        ser.is_valid(raise_exception=True)

        username = ser.validated_data['phone']
        password = ser.validated_data['password']
        try:
            user = User.objects.get(username=username)
        except:
            return Response('not found', status=status.HTTP_400_BAD_REQUEST)

        if user.check_password(password):
            token, _ = Token.objects.get_or_create(user=user)
            return Response(token.key, status=status.HTTP_200_OK)

        return Response('wrong password', status=status.HTTP_400_BAD_REQUEST)
