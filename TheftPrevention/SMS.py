import time
from typing import Tuple
from decouple import config
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

"""REST API Exception"""
class PhoneNumberVerificationError(Exception):
    pass
class OTPVerificationError(Exception):
    pass
class NoResponseError(Exception):
    pass

"""REST API Authentication"""
account_sid = config('SID')
auth_token  = config('TOKEN')
service_sid  = config('SERVICE_SID')


msg=\
"""
Notice from TheftPrevention

Your device has been DISCONNECTED!
"""


"""Instantiate REST API client"""
client = Client(account_sid, auth_token)


"""
Sends a text message to the user when the power is disconnected
Documentation: 
https://www.twilio.com/docs/sms/send-messages#post-parameters-conditional

Twilio phone number are code location: (anaheim, ca)

Parameters
----------
Void

Returns
-------
sid: String
    reponse from SMS client
"""
def send_sms(phone_number):    
    message = client.messages.create(
        to=phone_number,
        from_="+16572014198",
        body=msg
    )
    return message.sid


"""
Sends pings the users phoen so they can verify the device
Documentation:
https://www.twilio.com/docs/verify/api/verification#verification-response-properties

Parameters
----------
phone_number: String
    Device phone number, must be in E.164 format
    E.164: https://www.twilio.com/docs/glossary/what-e164
channel: String
    User can choose wether they want a call or text
    Default is set to text

Returns
-------
device_sid: String
    Device Sid (unique device identifyer)
"""
def send_verification_code(phone_number, channel='sms'):
    try:
        verification = client.verify \
            .services(service_sid) \
            .verifications \
            .create(
                to=phone_number,
                channel=channel)
        if verification is None:
            raise NoResponseError
        return verification
    except NoResponseError:
        print("There was no response from Twilio")

    except TwilioRestException:
        print("There was an error verifying the phone number")


"""
Verify the users phone number based on the code
Documentation:
https://www.twilio.com/docs/verify/api/verification-check?code-sample=code-check-a-verification-with-a-phone-number&code-language=Python&code-sdk-version=6.x

Parameters
----------
code: String
    OTP verification code

Returns
-------
status: String
    Status of verification
"""
def verify_code(code):
    try:
        verification_check = client.verify \
            .services(service_sid) \
            .verification_checks \
            .create(to='+19254378380', code=code)
        return verification_check.status

    except TwilioRestException as e:
        tmp = "There was an error verifying the confirmation code"
        print(tmp)
        # raise OTPVerificationError(tmp) from e


"""
Create a new Service int he Twilio API
Parameters
----------
name: String
    'friendly name' of account/alias

Returns
-------
response: String
    http request response
"""
def __create_new_service(name):
    print(name)
    return client.verify.services.create(friendly_name=name)


"""
Using flask and the Twilio API to respond to text messages sent to the bought Twilio number (anaheim, ca)
"""
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Thanks for letting us know you've received your laptop, we'll shut down the program now")

    return str(resp)



"""Function calls for testing"""
# print(verify_sms())
# print(send_sms())

# Garrett's Phone Number    +19254378380
# Ryan's Phone Number       +18582185453
# Nick's Phone Number       +16197726699