#Trigger used during sign in to custom check user input
#Backend requirement 4.2.13.7


import json


def lambda_handler(event, context):
    event['response']['autoConfirmUser'] = True
    event['response']['autoVerifyPhone'] = False
    event['response']['autoVerifyEmail'] = True

    return event