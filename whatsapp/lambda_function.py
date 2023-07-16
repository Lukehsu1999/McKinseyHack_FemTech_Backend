import json
import logging
import json
from twilio.rest import Client

SENDER = 'whatsapp:+14155238886'

def lambda_handler(event, context):
    print("recipients: ", event['recipients'])
    print("msg: ", event['msg'])

    # Read the file
    with open('auth.txt', 'r') as file:
        file_content = file.read()

    # Parse the JSON content into a dictionary
    auth = json.loads(file_content)

    # Twilio account credentials
    account_sid = auth['twilio_sid']
    auth_token = auth['twilio_secret_token']

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    recipients = event["recipients"]
    msg = event["msg"]

    # Send a WhatsApp message

    for recip in recipients:
        message = client.messages.create(
            body= msg,  # The message content
            from_= SENDER,  # Your Twilio WhatsApp number
            to= recip  # The recipient's phone number in WhatsApp format
        )
        print('Message sent successfully. SID:', message.sid)
