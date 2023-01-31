from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import AuthCode
from tools.serializers.verify_code_ser import VerifyCodeSer


class VerifyCode(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        ser = VerifyCodeSer(data=request.data)
        ser.is_valid(raise_exception=True)
        try:
            code = AuthCode.objects.get(id=ser.validated_data['code_id'])
        except:
            return Response('wrong id', status=status.HTTP_400_BAD_REQUEST)

        if code.code != ser.validated_data['code']:
            return Response('wrong code', status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=code.user)
        return Response(token.key, status=status.HTTP_200_OK)
