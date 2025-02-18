import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))  # Debugging log
        
        # Check if body exists in the request
        if 'body' not in event or not event['body']:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Invalid request. 'body' field is missing."}),
                'headers': {'Content-Type': 'application/json'}
            }

        # Parse JSON body
        data = json.loads(event['body'])

        # Validate taskName
        if 'taskName' not in data or not data['taskName'].strip():
            return {
                'statusCode': 400,
                'body': json.dumps({'error': "Invalid request. 'taskName' is required."}),
                'headers': {'Content-Type': 'application/json'}
            }

        # Create new task item
        task_id = str(uuid.uuid4())
        task = {
            'taskId': task_id,
            'taskName': data['taskName'].strip(),
            'completed': False
        }

        # Save to DynamoDB
        table.put_item(Item=task)

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Task added!', 'taskId': task_id}),
            'headers': {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'}
        }
    
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
