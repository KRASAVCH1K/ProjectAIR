from rest_framework import serializers
from func_app import encode_image
from api.models import wether_forecast


class ImageFromPillowSerializer(serializers.Serializer):
    image_base64 = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)
    encoding = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)