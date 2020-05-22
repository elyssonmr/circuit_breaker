import os

import requests
from requests.exceptions import Timeout

from circuit_breaker import circuit_breaker_function

service_url = os.environ['PLACE_ORDER_SERVICE_URL']


@circuit_breaker_function('place_order', 5, 300, (Timeout,))
def place_order(username, order_id):
    request_data = {
        "username": username,
        "number": order_id
    }

    response = requests.post(
        service_url + "/place_order",
        json=request_data,
        timeout=5
    )

    return response.json()
