from django.db import models

# Create your models here.
class wether_forecast:
    def __init__(self, image_base64, encoding):
        self.image_base64 = image_base64
        self.encoding = encoding
