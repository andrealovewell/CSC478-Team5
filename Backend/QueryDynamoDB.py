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
table = dynamodb.Table('JAMdb')

#handler for the lambda function
def lambda_handler(event, context):
    user=event['email']
    response = table.query(
        KeyConditionExpression=Key('User_Id').eq(user)
    )

    items =json.dumps((response['Items']))
    return items