from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Tool
from tools.serializers.get_tool_ser import GetToolSer


class GetToolView(APIView):
    def get(self, request, pk, *args, **kwargs):
        tools = Tool.objects.get(id=pk)
        ser = GetToolSer(tools)
        return Response(ser.data, status=status.HTTP_200_OK)
