from rest_framework.serializers import ModelSerializer

from tools.models import Recommend
from tools.serializers import FeatureSerializer
from tools.serializers.get_tool_ser import GetToolSer


class RecommendSerializer(ModelSerializer):
    tool = GetToolSer()
    feature = FeatureSerializer()

    class Meta:
        model = Recommend
        exclude = ['user']
