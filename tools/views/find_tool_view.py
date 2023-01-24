from rest_framework.views import APIView

from tools.serializers import TooPerfSerializer


class FindToolView(APIView):
    def create(self, request, *args, **kwargs):
        ser = TooPerfSerializer(self.request.data)
        ser.is_valid()
        
