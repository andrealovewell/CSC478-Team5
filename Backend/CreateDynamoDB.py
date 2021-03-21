# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
import botocore.exceptions
# import library to get current date
from datetime import date
from datetime import datetime
from time import gmtime, strftime

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('JAMDB')
today = date.today()
systemdate = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]


def returnResponse(code, message, data=None):
    return {
        'statusCode': code,
        'body': {
            'message': message,
            'data': data
        }
    }


# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # extract values from the event object we got from the Lambda service and store in a variable
    user = event['email']
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

    date = today.strftime("%m/%d/%y")  # requirement 3.2.1.1.4.1
    appId = systemdate

    # write to the DynamoDB table
    response = table.put_item(
        Item={
            'User_Id': user,
            'App_Id': appId,
            'Company': company,
            'Title': title,
            'Salary': salary,
            'Progress': progress,
            'Date': date,
            'JobLocation': location,
            'WebLink': weblink,
            'JobDescription': description,
            'JobRequirements': requirement,
            'PersonalReferences': references,
            'Notes': notes
        })

    print(response)

    return returnResponse(200, 'Creation was successful.', response)

