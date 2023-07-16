import json
import boto3

dataset = [
  {
    "uid": "1",
    "first name": "Abhimanyu",
    "last name": "Swaroop",
    "email": "as6434@columbia.edu",
    "number": "+12129616591",
    "moc": "Whatsapp",
    "user filter": "fintech"
  },
  {
    "uid": "2",
    "first name": "Anvi",
    "last name": "Agarwal",
    "email": "anvi.agarwal@columbia.edu",
    "number": "",
    "moc": "email",
    "user filter": "fintech"
  },
  {
    "uid": "3",
    "first name": "Luke",
    "last name": "Hsu",
    "email": "th2881@columbia.edu",
    "number": "",
    "moc": "email",
    "user filter": "fintech"
  },
  {
    "uid": "4",
    "first name": "Elena",
    "last name": "",
    "email": "pexy@seas.upenn.edu",
    "number": "+15512207773",
    "moc": "SMS",
    "user filter": "fintech"
  },
  {
    "uid": "5",
    "first name": "AbhiTwo",
    "last name": "Swaroop",
    "email": "as6434@columbia.edu",
    "number": "",
    "moc": "email",
    "user filter": "micro"
  },
  {
    "uid": "6",
    "first name": "ElenTwo",
    "last name": "",
    "email": "pexy@seas.upenn.edu",
    "number": "",
    "moc": "email",
    "user filter": "micro"
  }
]


def lambda_handler(event, context):
    # Convert the JSON data to lowercase for 'moc' values
    for item in dataset:
        item['moc'] = item['moc'].lower()

    # Extract user filters from the event object
    user_filters = event['userFilter']
    

    # Filter the data based on user filters
    filtered_data = []
    for user in dataset:
        if user['user filter'] in user_filters:
            filtered_data.append(user)
    
    print("filtered_data: ",filtered_data)
    # Extract phone numbers for SMS
    sms_list = [item['number'] for item in filtered_data if item['moc'] == 'sms' and item['number'] is not None]

    # Extract phone numbers for WhatsApp
    whatsapp_list = ['whatsapp:' + item['number'] for item in filtered_data if item['moc'] == 'whatsapp' and item['number'] is not None]

    # Extract email addresses
    email_list = [item['email'] for item in filtered_data if item['moc'] == 'email' and item['email'] is not None]

    msg = 'Title: '+event['title']+'\n'+'Event Description: '+event['description']+'\n'+'When: '+event['time']+'\n'+'Where: '+event['meetinglink']
    # TODO implement
    print(whatsapp_list, email_list, sms_list)
    print("msg: ", msg)
    
    # Create an AWS Lambda client
    lambda_client = boto3.client('lambda')
    
    # parameters for email
    email_parameter = {
        "recipients": email_list,
        "msg": msg
    }
    
    # Invoke the target Lambda function
    response = lambda_client.invoke(
        FunctionName='arn:aws:lambda:us-east-1:238592221641:function:func_sendEmail',
        InvocationType='Event',  # or 'RequestResponse' for synchronous invocation
        Payload=json.dumps(email_parameter)  # Optional payload to pass to the target Lambda function
    )
    
    # parameters for whatsapp
    sms_parameter = {
        "sender": "+18776586958",
        "recipients": sms_list,
        "msg": msg
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
        "recipients": whatsapp_list,
        "msg": msg
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
    
