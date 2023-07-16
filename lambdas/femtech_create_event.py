import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    
    # Create an AWS Lambda client
    lambda_client = boto3.client('lambda')
    
    # parameters for email
    email_parameter = {
        "recipients": ["th2881@columbia.edu", "anvi.agarwal@columbia.edu"],
        "msg": json.dumps(event)
    }
    
    # Invoke the target Lambda function
    response = lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:238592221641:function:func_sendEmail',
        InvocationType='Event',  # or 'RequestResponse' for synchronous invocation
        Payload=json.dumps(email_parameter)  # Optional payload to pass to the target Lambda function
    )
    
    print("Response from send Email", response)
    
    # parameters for whatsapp
    sms_parameter = {
        "sender": "+18776586958",
        "recipients": ["+15512207773"],
        "msg": json.dumps(event)
    }
    
    response = lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:238592221641:function:func_sendWhatsapp',
        InvocationType='Event',  # or 'RequestResponse' for synchronous invocation
        Payload=json.dumps(sms_parameter)  # Optional payload to pass to the target Lambda function
    )
    
    print("Response from send SMS", response)
    
    # parameters for whatsapp
    whatsapp_parameter = {
        "sender": "whatsapp:+14155238886",
        "recipients": ["whatsapp:+12129616591"],
        "msg": json.dumps(event)
    }
    
    response = lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:238592221641:function:func_sendWhatsapp',
        InvocationType='Event',  # or 'RequestResponse' for synchronous invocation
        Payload=json.dumps(whatsapp_parameter)  # Optional payload to pass to the target Lambda function
    )
    
    print("Response from send Whatsapp", response)
    
    
    
    return {
        'statusCode': 200,
        'body': event
    }
    
