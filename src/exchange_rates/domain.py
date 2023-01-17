from pydantic import BaseModel, Field


class ExchangeRatesResults(BaseModel):
    from_currency: str = Field(alias="1. From_Currency Code")
    to_currency: str = Field(alias="3. To_Currency Code")
    rate: str = Field(alias="5. Exchange Rate")


class AlphavantageResponse(BaseModel):
    results: ExchangeRatesResults = Field(alias="Realtime Currency Exchange Rate")


class ExchangeRatesServiceRequest(BaseModel):
    from_currency: str
    to_currency: str


class ExchangeRatesServiceResponse(BaseModel):
    rate: str
