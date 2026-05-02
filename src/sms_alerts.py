import os
from twilio.rest import Client

# Twilio configuration
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

def send_inventory_alert(to_phone, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        message = client.messages.create(
            to=to_phone,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )
        print(f'Alert sent successfully: {message.sid}')
    except Exception as e:
        print(f'Failed to send alert: {str(e)}')