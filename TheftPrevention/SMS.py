from decouple import config
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

"""REST API Authentication"""
account_sid = config('SID')
auth_token  = config('TOKEN')

"""Instantiate REST API client"""
client = Client(account_sid, auth_token)

"""
Sends a text message to the user when the power is disconnected

Parameters
----------
Void

Returns
-------
sid: String
    reponse from SMS client
"""
def send_sms(phone_number):
    print(phone_number)
    message = client.messages.create(
        #using garrett's phone number for testing
        to="+19254378380",
        #twilio phone number we bought (anaheim, ca)
        from_="+16572014198",
        body="Test"
    )
    return message.sid

"""
Dynamic-link phone number verification

Parameters
----------
Void

Returns
-------
status: Bool
    Authenticaction result
"""
def verify_sms():
    try:

        username = input("What would you like your username to be?: ")
        phone_number = input("What is your phone number?: ")

        validation_request = client.validation_requests.create(
                friendly_name=username,
                phone_number=phone_number
        )
        print(validation_request)
        return True
    
    except TwilioRestException as e:
        print(e)
        return False


"""
Check if the user alredy has credentials cached

Parameters
----------
name: String
    'friendly name' of account/alias

Returns
-------
response: String
    http request response
"""
def check_user(name):
    print(name)
    return client.verify.services.create(friendly_name=name)




"""Function calls for testing"""
# print(verify_sms())
# print(send_sms())