from django.urls import path, include

urlpatterns = [
    path("exchange-rates/", include("exchange_rates.urls")),
]