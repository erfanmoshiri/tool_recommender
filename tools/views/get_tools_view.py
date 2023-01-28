from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Tool
from tools.serializers.get_tool_ser import GetToolSer


class GetToolsView(APIView):
    def get(self, request, *args, **kwargs):
        tools = Tool.objects.all()
        ser = GetToolSer(tools, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
