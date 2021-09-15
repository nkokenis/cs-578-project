from SMS import send_sms
from SMS import verify_sms
from Alarm import play_alarm_mac
import sys
import psutil
import time


def detect_power():
    battery = psutil.sensors_battery()
    if(battery is None):
        print("This device does not have a battery. Exiting...")
        sys.exit(1)

    #need to dynamically verify the user's phone number before using it to send sms
    verify_sms()
    
    while(True):
        battery = psutil.sensors_battery()

        while(psutil.sensors_battery().power_plugged):
            print("Running on AC Power")
            time.sleep(1)
    
        send_sms("REPLACE WITH USER PHONE NUMBER")

        while(not psutil.sensors_battery().power_plugged):
            print("Running on Battery Power")
            time.sleep(1)

    

# Press the green button in the GUI to run the script.
if __name__ == '__main__':
    detect_power()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
