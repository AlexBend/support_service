import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from exchange_rates.services import get_alphavantage


@csrf_exempt
def convert(request):
    received_request = json.loads(request.body)
    from_currency = received_request["from"]
    to_currency = received_request["to"]
    response = get_alphavantage(from_currency, to_currency)
    return JsonResponse(response.dict())
