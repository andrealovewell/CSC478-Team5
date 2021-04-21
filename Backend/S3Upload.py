import json
import boto3
import base64

dynamodb = boto3.resource('dynamodb')
# use the DynamoDB object to select our table
table = dynamodb.Table('JAMDB')

# S3 resource and bucket connection
s3_client = boto3.client('s3')
bucket = 'jamdocuments'


def lambda_handler(event, context):
    user = event['email']
    appId = event['appID']
    filename = event['filename']
    filecontents = base64.b64decode(event['content'])

    print("Starting to write file")
    write_file_to_s3(filename, filecontents)
    print("Finished writing file")

    response = table.update_item(
        Key={
            'User_Id': user,
            'App_Id': appId,
        },

        UpdateExpression='SET S3_URL=:S3URL',

        ExpressionAttributeValues={
            ':S3URL': 'https://jamdocuments.s3-us-west-2.amazonaws.com/' + filename
        },

        ReturnValues="UPDATED_NEW"
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Upload Successful')
    }


# Writes file to S3 bucket
def write_file_to_s3(filename, filecontents):
    filename_with_path = filename

    s3_client = boto3.client('s3')
    s3_client.put_object(Body=filecontents, Bucket=bucket, Key=filename_with_path)


