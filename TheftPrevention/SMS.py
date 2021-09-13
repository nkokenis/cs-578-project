from twilio.rest import Client
from decouple import config

def send_sms():
    account_sid = config('SID')
    auth_token  = config('TOKEN')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+19254378380", 
        from_="+16572014198",
        body="Test")

    return message.sid

if __name__ == '__main__':
    print(send_sms())