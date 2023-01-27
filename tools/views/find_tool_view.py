from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Feature
from tools.serializers import TooPerfSerializer
from tools.utils import get_top


class FindToolView(APIView):
    def post(self, request, *args, **kwargs):
        ser = TooPerfSerializer(data=self.request.data)
        ser.is_valid()
        ids = ser.validated_data['features']
        feat = Feature.objects.filter(id__in=ids).values_list('name', flat=True)
        tools = get_top(feat)
        return Response(tools, status=status.HTTP_200_OK)

