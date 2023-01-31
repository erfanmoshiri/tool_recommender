import random

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import AuthCode
from tools.serializers import RegisterUserSer
from tools.utils import send_code


class RegisterUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ser = RegisterUserSer(data=request.data)
        ser.is_valid(raise_exception=True)
        if ser.exists():
            return Response('exists', status=status.HTTP_400_BAD_REQUEST)

        user = ser.create(ser.validated_data)
        c = random.randint(1000, 9999)
        code = AuthCode.objects.create(code=c, user=user)
        send_code(user.username, c)
        return Response({'code_id': code.id}, status=status.HTTP_200_OK)
