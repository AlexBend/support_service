import requests
from django.conf import settings
from django.http import JsonResponse
from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    from_currency: str = Field(alias="1. From_Currency Code")
    to_currency: str = Field(alias="3. To_Currency Code")
    rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


def convert(request):
    from_currency = "USD"
    to_currency = "EUR"
    url = (
        f"{settings.ALPHA_VANTAGE_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&to_currency={to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    )
    response = requests.get(url)
    alphavantage_response = AlphavantageResponse(**response.json())

    return JsonResponse(alphavantage_response.dict())
