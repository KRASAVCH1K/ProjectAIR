import func_app
from api.models import wether_forecast
from rest_framework.response import Response

from .serializers import ImageFromPillowSerializer
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema


# Create your views here.
class imageFromPillowView(APIView):
    @extend_schema(request=ImageFromPillowSerializer, responses=ImageFromPillowSerializer)

    def get(self, request, days, color):
        # days = request.GET.get('days')
        # color = request.GET.get('color')

        image_string = func_app.encode_image(days,color)
        image_result = wether_forecast(image_string, 'utf-8')
        serializer_for_request = ImageFromPillowSerializer(instance=image_result)

        return Response(serializer_for_request.data)