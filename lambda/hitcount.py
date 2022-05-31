import json
import os
from urllib import response

import boto3

dynamoDB_resc = boto3.resource('dynamodb')
table = dynamoDB_resc.Table(os.environ['HITS_TABLE_NAME'])
lambda_client = boto3.client('lambda')

def handler(event, context):
    print('request {}' .format(json.dumps(event)))
    table.update_item(
        Key={'path' : event['path']},
        UpdateExpression='ADD hits :incr', 
        ExpressionAttributeValues={':incr': 1}
    )

    response = lambda_client.invoke(
        FunctionName = os.environ['DOWNSTREAM_FUNCTION_NAME'],
        Payload=json.dumps(event)
    )

    body = response['Payload'].read()

    print ('downstream response: {}' .format(body))

    return json.loads(body)