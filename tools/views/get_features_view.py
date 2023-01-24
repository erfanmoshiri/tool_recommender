from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Feature
from tools.serializers.feature_serializer import FeatureSerializer


class GetFeaturesView(APIView):
    def get(self, request, *args, **kwargs):
        features = Feature.objects.all()
        ser = FeatureSerializer(features)
        return Response(ser.data, status=status.HTTP_200_OK)
