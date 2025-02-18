import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    response = table.scan()
    tasks = response.get('Items', [])  # Extract tasks properly

    return {
        'statusCode': 200,
        'body': json.dumps(tasks),  # Ensure JSON array, not string
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
