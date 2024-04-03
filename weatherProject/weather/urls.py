from django.urls import path
from .views import weather_microservice

urlpatterns = [
    path('weather/', weather_microservice, name='weather_microservice'),
]