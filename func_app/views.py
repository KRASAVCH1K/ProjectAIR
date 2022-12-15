from django.http import HttpResponse
from weather.funk_1 import weather
import base64


# Create your views here.

def encode_image(days, color):
    image_path = weather(days, color)
    with open(image_path, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encode_data = base64.b64encode(binary_file_data)[:20]
        base64_massage = base64_encode_data.decode('utf-8')
    return base64_massage


def index(request):
    days = request.GET.get('days')
    color = request.GET.get('color')
    return HttpResponse(f'{encode_image(days, color)}')
