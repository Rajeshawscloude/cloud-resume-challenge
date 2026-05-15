import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-count')

def lambda_handler(event, context):
    
    # Get current count
    response = table.get_item(
        Key={'id': 'visitors'}
    )
    
    # Increase count by 1
    count = response['Item']['count'] + 1
    
    # Save new count
    table.update_item(
        Key={'id': 'visitors'},
        UpdateExpression='SET #cnt = :val',
        ExpressionAttributeNames={'#cnt': 'count'},
        ExpressionAttributeValues={':val': count}
    )
    
    # Return count
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': str(count)})
    }
