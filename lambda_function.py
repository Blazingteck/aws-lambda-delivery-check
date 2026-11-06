import base64
import json
import math


def response(status_code, data):
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }


def lambda_handler(event, context):
    order = event

    if "requestContext" in event:
        try:
            body = event.get("body") or "{}"

            if event.get("isBase64Encoded"):
                body = base64.b64decode(body, validate=True)

            order = json.loads(body)
        except (ValueError, UnicodeError):
            return response(400, {"error": "Send valid JSON."})

    if not isinstance(order, dict):
        return response(400, {"error": "Send a JSON object."})

    if "order_amount" not in order:
        return response(400, {
            "error": "Please provide the order amount."
        })

    amount = order["order_amount"]

    if type(amount) not in (int, float):
        return response(400, {
            "error": "Order amount must be a number."
        })

    if isinstance(amount, float) and not math.isfinite(amount):
        return response(400, {
            "error": "Order amount must be a finite number."
        })

    if amount < 0:
        return response(400, {
            "error": "Order amount cannot be negative."
        })

    return response(200, {
        "order_amount": amount,
        "currency": "NGN",
        "free_delivery": amount >= 10000
    })
