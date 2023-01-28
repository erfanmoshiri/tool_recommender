from rest_framework.serializers import ModelSerializer

from tools.models import Tool


class GetToolSer(ModelSerializer):
    class Meta:
        model = Tool
        fields = '__all__'
