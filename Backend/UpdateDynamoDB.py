#Update a record in the database
#Backend requirement 4.2.13.3

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


# handler for the lambda function
def lambda_handler(event, context):
    # extract values from the event object we got from the Lambda service and store in a variable
    user = event['email']
    appID = event['appID']
    company = event['company']
    title = event['position']
    salary = event['salary']
    progress = event['progress']
    location = event['location']
    weblink = event['weblink']
    description = event['description']
    requirement = event['requirement']
    references = event['references']
    notes = event['notes']

    response = table.update_item(
        Key={
            'User_Id': user,
            'App_Id': appID,
        },

        UpdateExpression='SET Company=:C, Title=:T, Salary =:S, Progress=:P, JobLocation=:L, WebLink=:W, JobDescription= :Jdesc, JobRequirements= :Jreq, PersonalReferences=:R, Notes =:N',

        ExpressionAttributeValues={
            ':C': company,
            ':T': title,
            ':S': salary,
            ':P': progress,
            ':L': location,
            ':W': weblink,
            ':Jdesc': description,
            ':Jreq': requirement,
            ':R': references,
            ':N': notes
        },

        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': "Record has been updated"
    }
