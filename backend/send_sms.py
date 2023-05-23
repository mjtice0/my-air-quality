# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "REDACTED"
auth_token = "REDACTED"
client = Client(account_sid, auth_token)
def send_sms(aqi):
    message = client.messages \
        .create(
            body="Your local AQI is 100",
            from_='+18667164824',
            to='+17195819254'
            )

    print(message.sid)