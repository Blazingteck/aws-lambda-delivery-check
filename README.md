# AWS Lambda Delivery Eligibility Checker

A Python function deployed on AWS Lambda that checks whether an order qualifies for free delivery.

## Project purpose

This project demonstrates serverless code execution, input validation, and testing through the AWS Lambda console.

Orders of NGN 10,000 or more qualify for free delivery.

## Technologies used

- AWS Lambda
- Python 3.14
- JSON test events

## How it works

1. The function receives an event containing an order amount.
2. It checks that the amount is provided, is a number, and is not negative.
3. It compares the amount with the NGN 10,000 threshold.
4. It returns the order amount, currency, and delivery eligibility.

Invalid amounts receive a clear error message.

## Example input

    {
      "order_amount": 12000
    }

## Example response

    {
      "order_amount": 12000,
      "currency": "NGN",
      "free_delivery": true
    }

## Verified test results

| Input | Expected and observed result |
|---|---|
| NGN 12,000 | Free delivery is true |
| NGN 8,000 | Free delivery is false |
| NGN 10,000 | Free delivery is true |
| Missing order amount | Please provide the order amount. |
| Negative order amount | Order amount cannot be negative. |

The code also validates nonnumeric amounts.

## Deployment and testing

1. Create an AWS Lambda function using Python 3.14.
2. Replace the contents of lambda_function.py with the code in this repository.
3. Set the handler to lambda_function.lambda_handler.
4. Deploy the code.
5. Open the Test tab and enter a JSON event.
6. Run the test and inspect the response.

## Current scope

The function has been deployed and tested using direct JSON events in the AWS Lambda console.

## Planned enhancement

Connect the function to Amazon API Gateway and adapt it to process HTTP requests and return HTTP responses.
