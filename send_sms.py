# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client 
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
def send_sms(aqi):
    message = client.messages \
        .create(
            body=f"Your local AQI is {aqi}",
            from_='+18667164824',
            to='+17195819254'
            )

    print(message.sid)