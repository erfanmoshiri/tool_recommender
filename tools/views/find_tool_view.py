from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Feature, Recommend
from tools.serializers import TooPerfSerializer
from tools.utils import get_top


class FindToolView(APIView):
    # authentication_classes =
    def post(self, request, *args, **kwargs):
        ser = TooPerfSerializer(data=self.request.data)
        ser.is_valid()
        ids = ser.validated_data['features']
        feat = Feature.objects.filter(id__in=ids).values_list('name', flat=True)
        tool_ids = get_top(feat)

        request.user.recommends.all().delete()
        new_recs = []
        for feat in ids:
            for tool in tool_ids:
                new_recs.append(
                    Recommend(
                        user=request.user,
                        tool_id=tool,
                        feature_id=feat
                    )
                )
        # new_recs = [
        #     [
        #         Recommend(
        #             user=request.user,
        #             tool_id=tool,
        #             feature_id=feat
        #         )
        #         for tool in tool_ids
        #     ]
        #     for feat in ids
        # ]
        Recommend.objects.bulk_create(new_recs)
        return Response(tool_ids, status=status.HTTP_200_OK)
