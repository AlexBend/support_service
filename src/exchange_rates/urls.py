from django.urls import path
from src.exchange_rates.api import convert

urlpatterns = [
    path("convert/", convert),
]
