def lambda_handler(event, context):
    if "order_amount" not in event:
        return {"error": "Please provide the order amount."}

    order_amount = event["order_amount"]

    if type(order_amount) not in (int, float):
        return {"error": "Order amount must be a number."}

    if order_amount < 0:
        return {"error": "Order amount cannot be negative."}

    return {
        "order_amount": order_amount,
        "currency": "NGN",
        "free_delivery": order_amount >= 10000
    }
