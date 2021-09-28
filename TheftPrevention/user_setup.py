import time
import SMS as sms
import update_cache
from driver import UserFailError

"""
-> Function: check_status
Check the status of the verification code
->Parameters:
phone_number: String
    users phone number
fail_count: int
    user errors on current thread
->Returns:
status: Boolean
    verification status of user
fail_count: int
    updates fail count on thread
"""
def check_status(phone_number,fail_count):
    while True:
        if fail_count >= 4:
            raise UserFailError

        opt = input('Enter your verification code: ')
        val = sms.verify_code(phone_number,opt)

        if val == "approved":
            return True,0
        elif val == "pending":
            print("Incorrect code, please try agian.")
            fail_count+=1
        else:
            return False,fail_count


"""
-> Function: user_setup
Verify user's phone number
-> Parameters:
N/A
-> Returns:
N/A
"""
def verify():
    fail_count = 0
    phone_number = ""
    sid = ""
    approved = False
    while True:
        if fail_count >= 4:
            raise UserFailError

        phone_number = input('Enter your phone number: ')
        sid = sms.send_verification_code(phone_number,'sms')

        update_cache("verification_sid",sid)

        print("Sending code...")
        time.sleep(3)
        
        approved, fail_count = check_status(phone_number,fail_count)
        if approved:
            print("Approved!")
            break
        elif not approved:
            print("The verification period timed out. Please try again.")


