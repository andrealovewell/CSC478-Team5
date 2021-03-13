import json
# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
from boto3.dynamodb.conditions import Key, Attr
import decimal

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('JAMDB')


def lambda_handler(event, context):
    user = event['email']
    appID = event['appID']

    table.delete_item(
        Key={
            'User_Id': user,
            'App_Id': appID,
        },
    )
    return {
        'statusCode': 200,
        'body': "Record has been deleted"
    }
