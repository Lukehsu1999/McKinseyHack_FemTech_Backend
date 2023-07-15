import json
import boto3
from botocore.exceptions import ClientError
import logging

# static variables for send_email
SENDER = "th2881@columbia.edu"
AWS_REGION = "us-east-1"

def lambda_handler(event, context):
    print("event: ", event)
    print("context: ", context)
    def send_email(recipient, data):
        # recipient: (string) email address
        # data: (dict) restaurant information
        SUBJECT = "Restaurant Recommendation from Dining Concierge"
        BODY_TEXT = "default_body_text"
        #### TODO: parse data into Body text ###
        
        CHARSET = "UTF-8"
        client = boto3.client('ses',region_name=AWS_REGION)
        try:
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        recipient,
                    ],
                },
                Message={
                    'Body': {
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                            },
                    },
                    'Subject':{
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
        return
    
    sampleResData = {
        "resname": "Good to eat"
    }
    send_email("th2881@columbia.edu", sampleResData)