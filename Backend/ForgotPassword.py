#Update user password for login
#Backend requirement 4.2.13.9

import json
import boto3
import botocore.exceptions
import os
import hmac
import hashlib
import base64
import uuid

# client ID per the JAM USER POOL in Coginto
CLIENT_ID = '2n4teurhe9h9bpih8fl515l157'


# establishes connection to congito and obtains secret hash
def get_secret_hash(username):
    msg = username + os.environ['clientId']
    dig = hmac.new(str(os.environ['clientSecret']).encode('utf-8'),
                   msg=str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2


def lambda_handler(event, context):
    client = boto3.client('cognito-idp')

    # checks if username is in the user pool
    try:
        username = event['username']
        response = client.forgot_password (
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
        )
    except client.exceptions.UserNotFoundException:
        return {
            "message": "Username doesnt exists"
        }
    return {
        "message": f"Please check your Registered email id for validation code"
    }