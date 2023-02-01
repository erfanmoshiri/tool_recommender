import random

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import AuthCode
from tools.serializers import LoginUserSer
from tools.utils import send_code


class LoginUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ser = LoginUserSer(data=request.data)
        ser.is_valid(raise_exception=True)
        if not (user := ser.exists()):
            return Response('not found', status=status.HTTP_400_BAD_REQUEST)

        c = random.randint(1000, 9999)
        # c = 1111
        code = AuthCode.objects.create(code=c, user=user)
        send_code(user.username, c)
        return Response({'code_id': code.id}, status=status.HTTP_200_OK)
