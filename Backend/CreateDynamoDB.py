# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import library to get current date
from datetime import date

# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('JAMdb')
today = date.today()


# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # extract values from the event object we got from the Lambda service and store in a variable
    user = event['email']
    company = event['company']
    title = event['position']
    progress = event['progress']
    location = event['location']
    weblink = event['weblink']
    description = event['description']
    requirement = event['requirement']
    references = event['references']
    notes = event['notes']

    date = today.strftime("%m/%d/%y")  # requirement 3.2.1.1.4.1

    # write to the DynamoDB table
    response = table.put_item(
        Item={
            'User_Id': user,
            'Company#Title#Progress#Date': company + title + progress + date,
            'Location': location,
            'Web Link': weblink,
            'Job Descriptions': description,
            'Job Requirements': requirement,
            'References': references,
            'Notes': notes
        })
    # return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps({'User': user, 'Company': company, 'Title': title, 'Progress': progress,
                            'Date': date, 'Location': location, 'Web Link': weblink, 'Job Descriptions': description,
                            'Job Requirements': requirement, 'References': references, 'Notes': notes}, sort_keys=True,
                           indent=3)
    }