from Text import text
from SMS import *
from power_detection import main
import traceback
import sys
import os
import time

class UserFailError(Exception):
    pass
class InvalidArguments(Exception):
    pass
class SystemExit(Exception):
    pass

def user_setup():
    fail_count = 0
    pending = False
    phone_number = ""
    while True:
        if not pending:
            phone_number = input('Enter your phone number: ')
        
        result = send_verification_code(phone_number)
        print(result.status)

        if fail_count >= 4:
            raise UserFailError
        elif result.status is None:
            print("Please check your phone number and try again.")
            fail_count+=1
            print(fail_count)
        elif result.status == "pending":
            pending = True
            print("Waiting for code to be sent...")
            time.sleep(15)
        else:
            print("Code sent.")
            break
    fail_count = 0
    opt = input('Enter your verification code: ')
    while True:
        val = verify_code(phone_number,opt)
        if fail_count >= 4:
            raise UserFailError
        elif val == "approved":
            print("Approved!")
            break
        elif val == "pending":
            print("Waiting for verification result...")
        else:
            print("Verification Failed please try again.")
            opt = input('Enter your verification code: ')
        time.sleep(15)


def main():
    try:
        args = sys.argv
        if len(args) == 1:
            print("Call terminal")
        elif len(args) == 2 and args[1] == '-g':
            print("Call GUI")
        else:
            raise InvalidArguments
    
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
            
        
        else:
            print("\n\nOkay lets get you {}certified!{}\n".format(text.ITALIC,text.ENDC))
            user_setup()

    except InvalidArguments:
        print(text.driver_argument_error)
        raise SystemExit

    except KeyboardInterrupt:
        print("\n\nUser stopped program with Keybaord Interrupt.\n\n")
        raise SystemExit

    except NoResponseError:
        print("\n\nThere was no response from the Twilio REST API")
        print("Please try again.\n\n")
        raise SystemExit

    except UserFailError:
        print("\n\nYou have failed to many times")
        print("Please restart the program and try again\n\n")
        raise SystemExit
        
    except SystemExit:
        print("Shutting down...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

    except Exception:
        print(traceback.format_exc())
        print("Shutting down...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

if __name__ == "__main__": main()