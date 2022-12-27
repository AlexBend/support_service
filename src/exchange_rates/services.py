import requests
from django.conf import settings
from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    Exchange_Rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


def get_alphavantage(from_currency, to_currency):
    url = (
        f"{settings.ALPHA_VANTAGE_BASE_URL}/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={from_currency}&to_currency={to_currency}&apikey={settings.ALPHA_VANTAGE_API_KEY}"
    )
    response = requests.get(url)
    alphavantage_response = AlphavantageResponse(**response.json())
    return alphavantage_response
