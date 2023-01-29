from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tools.models import Recommend


class RateToolView(APIView):
    def post(self, request, pk, *args, **kwargs):
        try:
            rec = Recommend.objects.get(id=pk)
        except:
            return Response('not found', status=status.HTTP_400_BAD_REQUEST)

        rec.liked = bool(request.query_params.get('rate', None))
        rec.save()
        return Response(rec.liked, status=status.HTTP_200_OK)

    pass
