# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/update-status', methods=['POST'])
def json_example():
    request_data = request.get_json()

    status = request_data['SmsStatus']

    return status

# If you need to format the data return this:
# '''
# SMS status: {}
# From endpoint: {}'''.format(status, endpoint)

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)




"""
This is a test POST request that Twilio will send

curl -d '{
    "SmsSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "SmsStatus": "delivered",
    "MessageStatus": "delivered",
    "To": "+15558675310",
    "MessageSid": "SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "AccountSid": "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "From": "+15017122661",
    "ApiVersion": "2010-04-01"
}'\
    -H 'Content-Type: application/json'\
    -X POST http://127.0.0.1:5000/update-status
    
"""