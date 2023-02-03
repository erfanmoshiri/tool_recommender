from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Recommend
from tools.utils.recommender import add_to_cell


class RateToolView(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            rec = Recommend.objects.get(id=pk)
        except:
            return Response('not found', status=status.HTTP_400_BAD_REQUEST)
        if rec.user_id != request.user.id:
            return Response('', status=status.HTTP_401_UNAUTHORIZED)

        rec.liked = bool(int(request.query_params.get('rate', None)))
        rec.save()

        # success = add_to_cell(
        #     rec.tool.id,
        #     rec.feature.name,
        #     rec.liked
        # )
        success = True
        return Response(success, status=status.HTTP_200_OK)

    pass
