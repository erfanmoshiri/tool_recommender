from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.serializers import RecommendSerializer


class GetRecommendView(APIView):
    def get(self, request, *args, **kwargs):
        recommends = request.user.recommends.all()
        ser = RecommendSerializer(recommends, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
