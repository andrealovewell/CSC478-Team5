#import the json utility package
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3


# create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('JAMdb')

# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
# extract values from the event object we got from the Lambda service and store in a variable
    user = event['email']
    company = event['company']
    title = event['title']
    progress = event['progress']
    date = event['date']
# write to the DynamoDB table
    response = table.put_item(
        Item={
            'User_Id': user,
            'Company#Title#Progress#Date':company + title + progress + date,
            })
# return a  JSON object
    return {
        'statusCode': 200,
        'body': json.dumps({'User': user, 'Company': company, 'Title': title, 'Progress': progress,
             'Date': date}, sort_keys=True, indent=3)
     }