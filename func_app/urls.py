from django.urls import path
from func_app import views

urlpatterns = [
    path('base64', views.index),
]
