import sys
import os
import time
import traceback
from Text import text
import SMS
import user_setup
import power_detection

""" User defined Errors """
class UserFailError(Exception):
    pass
class InvalidArguments(Exception):
    pass
class SystemExit(Exception):
    pass

""" Terminal Greeting """
def intro_text():
    print("\n"+text.line)
    print(text.graphic)
    print(text.line)
    print(text.msg.format(text.ITALIC,text.CGREEN2,text.BOLD,text.ENDC))
    print("Lets get you setup so you can be ",end="")
    print("{}{}PROTECTED{}"\
        .format(text.CGREEN2,text.BOLD,text.ENDC))

    # If cache exists, ask if they want same phone number
    
    res = input("\n\nHave you already setup an account with Theft Prevention before? [yes or no]: ")
    res = res.lower()

    if('y' in res):
        print("\n\nThanks for your support :)\n\nThe program is booting up...\n\n")
    else:
        print("\n\nOkay lets get you {}certified!{}\n".format(text.ITALIC,text.ENDC))
        user_setup.verify()
    
    adapter = power_detection.AC_Adapter()
    adapter.addUnpluggedListener(power_detection.take_photo)
    adapter.addUnpluggedListener(power_detection.send_sms)
    success = adapter.listen()

    if not success:
        print("Device does not have battery. Exiting...")
        sys.exit(1)

"""
-> Function: main
main driver of the program
catch all program errors and exit here
-> Parameters:
N/A
-> Returns:
Errors: Exception
    Any errors occured
"""
def main():
    try:
        print("Starting Flask Server...")
        os.system("python app.py &")
        time.sleep(5)
        
        args = sys.argv
        if len(args) == 1:
            intro_text()
        elif len(args) == 2 and args[1] == '-g':
            print("Call GUI")
        else:
            raise InvalidArguments
    
    except InvalidArguments:
        print(text.driver_argument_error)
        print(text.turn_off)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

    except KeyboardInterrupt:
        print("\n\nUser stopped program with Keybaord Interrupt.\n\n")
        print(text.turn_off)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

    except SMS.NoResponseError:
        print("\n\nThere was no response from the Twilio REST API")
        print("Please try again.\n\n")
        print(text.turn_off)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

    except UserFailError:
        print("\n\nYou have failed to many times")
        print("Please restart the program and try again\n\n")
        print(text.turn_off)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)
        
    except SystemExit:
        print(text.turn_off)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(1)

    except Exception:
        print(traceback.format_exc())
        os._exit(1)

if __name__ == "__main__": main()
