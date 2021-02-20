import json


def lambda_handler(event, context):
    event['response']['autoConfirmUser'] = True
    event['response']['autoVerifyPhone'] = False
    event['response']['autoVerifyEmail'] = True

    return event