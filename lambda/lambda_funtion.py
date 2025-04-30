# lambda/lambda_function.py

import os
import boto3

def handler(event, context):
    bucket_name = os.environ["BUCKET_NAME"]
    return {
        "statusCode": 200,
        "body": f"Hello from Lambda! Using bucket {bucket_name}"
    }