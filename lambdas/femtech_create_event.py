import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    # Create an AWS Lambda client
    lambda_client = boto3.client('lambda')
    
    # parameters for email
    parameter = {
        "recipients": ["th2881@columbia.edu"],
        "msg": event
    }
    
    # Invoke the target Lambda function
    response = lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:238592221641:function:func_sendEmail',
        InvocationType='Event',  # or 'RequestResponse' for synchronous invocation
        Payload=json.dumps(parameter)  # Optional payload to pass to the target Lambda function
    )
    
    
    
    
    return {
        'statusCode': 200,
        'body': event
    }
    
