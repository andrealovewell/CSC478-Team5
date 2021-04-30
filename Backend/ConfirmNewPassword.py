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

#verifies code sent by previous lambda function and username. Allows user to enter new  password
    try:
        username = event['username']
        password = event['password']
        code = event['code']
        client.confirm_forgot_password(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            ConfirmationCode=code,
            Password=password,
        )
    except client.exceptions.UserNotFoundException as e:
        return {
                "error": True,
                "success": False,
                "data": None,
                "message": "Username doesnt exists"
             }

    except client.exceptions.CodeMismatchException as e:
        return {
                "error": True,
                "success": False,
                "data": None,
                "message": "Invalid Verification code"
             }

    return {
            "error": False,
            "success": True,
            "message": f"Password has been changed successfully",
            "data": None
         }