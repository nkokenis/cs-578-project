from decouple import config
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

""" REST API Exception """
class PhoneNumberVerificationError(Exception):
    pass
class NoResponseError(Exception):
    pass
class sms:

    """ REST API Authentication """
    account_sid = config('SID')
    auth_token  = config('TOKEN')
    global sms_sid
    sms_sid = config('SMS_SID')

    """ Instantiate REST API client """
    global client 
    client = Client(account_sid, auth_token)

    """
    Function:
    Send SMS

    Description:
    Sends a text message to the user when the power is disconnected

    Documentation: 
    https://www.twilio.com/docs/sms/send-messages#post-parameters-conditional

    Parameters:
    N/A

    Returns:
    sid: String
        response from SMS client
    """
    def send_sms(self,phone_number):
        msg=\
        """
        Notice from TheftPrevention

        Your device has been disconnected!
        """
        message = client.messages.create(
            to=phone_number,
            from_="+16572014198",
            body=msg
        )
        return message.sid

    """
    Function:
    Send Verification Code

    Description:
    Pings the user's phone so they can verify the current device

    Documentation:
    https://www.twilio.com/docs/verify/api/verification#verification-response-properties

    Parameters:
    phone_number: String
        Device phone number, must be in E.164 format
        E.164: https://www.twilio.com/docs/glossary/what-e164
    channel: String
        User can choose wether they want a call or text
        Default is set to text

    Returns:
    device_sid: String
        Device SID (unique device identifyer)
    """
    def send_verification_code(self,phone_number, channel='sms'):
        try:
            verification = client.verify \
                .services(sms_sid) \
                .verifications \
                .create(
                    to=phone_number,
                    channel=channel,
                    status_callback="http://127.0.0.1:5000/update-status")
                
            # Wait until status from Flask REST API!!!!!!!!!
            return verification

        except TwilioRestException as e:
            print("There was an error verifying the phone number")
            print(e)

    """
    Fucntion:
    Verify Code

    Description:
    Verify the user's phone number based on the code

    Documentation:
    https://www.twilio.com/docs/verify/api/verification-check?code-sample=code-check-a-verification-with-a-phone-number&code-language=Python&code-sdk-version=6.x

    Parameters:
    code: String
        OTP verification code

    Returns:
    status: String
        Status of the verification
    """
    def verify_code(self,phone_number,code):
        try:
            verification_check = client.verify \
                .services(sms_sid) \
                .verification_checks \
                .create(to=phone_number, code=code)
            return verification_check

        except TwilioRestException as e:
            tmp = "There was an error verifying the confirmation code\n\n"
            print(tmp)
            print(e)


    """Function calls for testing"""
    # print(verify_sms())
    # print(send_sms())

    # phone_number = input("Phone Number: ")
    # res = send_verification_code(phone_number)
    # print(res)
    # code = input("code: ")
    # print(verify_code(phone_number,code))

    # Garrett's Phone Number    +19254378380
    # Ryan's Phone Number       +18582185453
    # Nick's Phone Number       +16197726699
    # Twilio Phone NUmber       +16572014198