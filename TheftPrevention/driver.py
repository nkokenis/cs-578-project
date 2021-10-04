import os
import sys
import SMS
import traceback
import user_setup
from Text import text
import power_detection
from cache import access_cache

""" User defined Errors """
class UserFailError(Exception):
    pass
class InvalidArguments(Exception):
    pass
class SystemExit(Exception):
    pass

""" Graphic """
def print_graphic():
    print("\n"+text.line)
    print(text.graphic)
    print(text.line+"\n")
    

""" Terminal Greeting """
def intro_text():
    print(text.msg.format(text.ITALIC,text.CGREEN2,text.BOLD,text.ENDC))
    print("Lets get you setup so you can be ",end="")
    print("{}{}PROTECTED{}\n\n"\
        .format(text.CGREEN2,text.BOLD,text.ENDC))
    user_setup.verify()
    

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
        # os.system("python app.py &")
        # time.sleep(3)
        print_graphic()
        args = sys.argv
        version = None
        if len(args) == 1:
            version = "text"
        elif len(args) == 2 and args[1] == '-g':
            version = "gui"
        else:
            raise InvalidArguments

        quick_start = access_cache("phone_number")
        name = access_cache("name")

        if quick_start is None or name is None and version == "text":
            intro_text()
        elif quick_start is None or name is None and version == "gui":
            print("call gui")
        else:
            msg = "\n\nHello {}! run program with phone number: {}? [yes] or [no]: ".format(name, quick_start)
            res = input(msg)
            res.lower()
            if "n" in res:
                intro_text()
            else:
                print(text.welcome)
        
        print("The program is booting up...\n\n")
        
        adapter = power_detection.AC_Adapter()
        #adapter.addUnpluggedListener(power_detection.play_alarm)
        adapter.addUnpluggedListener(power_detection.take_photo)
        adapter.addUnpluggedListener(power_detection.send_sms)
        
        success = adapter.listen()

        if not success:
            print("Device does not have battery. Exiting...")
            sys.exit(1)
    
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
