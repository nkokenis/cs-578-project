from twilio.rest import Client
from decouple import config
import os

"""
we need to make the phone numbers dynamic to the user

use this documentation: https://www.twilio.com/docs/verify/api/service
to verify a user's phone number
"""

#sends a text message to the user when the power is disconnected
def send_sms():
    account_sid = config('SID')
    auth_token  = config('TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        #using garrett's phone number for testing
        to="+19254378380",
        #twilio phone number we bought (anaheim, ca)
        from_="+16572014198",
        body="Test")

    return message.sid

#dynamic-link phone number verification
def verify_sms():
    return -1

if __name__ == '__main__':
    print(send_sms())