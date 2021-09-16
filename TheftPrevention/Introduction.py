from Text import text
from SMS import *
import traceback
import sys
import os

class UserFailError(Exception):
    pass

def user_setup():
    fail_count = 0
    pending = False
    while True:
        if not pending:
            phone_number = input('Enter your phone number: ')
        
        result = send_verification_code(phone_number)
        
        if fail_count >= 4:
            raise UserFailError
        elif result.status is None:
            print("Please check your phone number and try again.")
            fail_count+=1
            print(fail_count)
        elif result.status == "pending":
            print("Waiting for code to be sent...")
            time.sleep(5)
        else:
            print("Code sent.")
            break
    fail_count = 0
    opt = input('Enter your verification code: ')
    while True:
        val = verify_code(opt)
        if fail_count >= 4:
            UserFailError
        elif val == "approved":
            print("Approved!")
            break
        elif val == "pending":
            print("Waiting for verification result...")
        else:
            print("Verification Failed please try again.")
            opt = input('Enter your verification code: ')
        time.sleep(5)


def main():
    try:
        print("\n"+text.line)
        print(text.graphic)
        print(text.line)
        print(text.msg.format(text.ITALIC,text.CGREEN2,text.BOLD,text.ENDC))
        print("Lets get you setup so you can be ",end="")
        print("{}{}PROTECTED{}"\
            .format(text.CGREEN2,text.BOLD,text.ENDC))

        res = input("\n\nHave you already setup an account with Theft Prevention before? [yes or no]: ")
        res = res.lower()

        if('y' in res):
            print("\n\nThanks for your support :)\n\nThe program is booting up...\n\n")

        # elif('i' in res):
        #     name = input("Please enter your username: ")
        #     if check_user(name) is not None:
        #         print("You are already authenticated")
        #     else:
        #         print("No authentication present")
        #         print("\n\nNo worries, lets get you set up!\n\n")
        #         verify_sms()
        
        else:
            print("\n\nOkay lets get you {}certified!{}\n".format(text.ITALIC,text.ENDC))
            user_setup()

    
    except KeyboardInterrupt:
        print("\nUser stopped program with Keybaord Interrupt.\nShutting down...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
    except NoResponseError:
        print("There was no response from the Twilio REST API")
        print("Please try again.\n\n")
        print("Shutting down...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
    except UserFailError:
        tmp = "\n\nYou have failed to many times, please restart the program and try again\n"
        print(tmp)
        print("Shutting down...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
    except Exception:
        print(traceback.format_exc())
        print("Shutting down...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)

if __name__ == "__main__": main()

# 6572014198