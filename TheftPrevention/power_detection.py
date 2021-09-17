from SMS import send_sms
from SMS import verify_code
from Alarm import play_alarm_mac
from Camera import open_camera
import sys
import psutil
import time

"""
Function:
Detect Power

def detect_power(phone_number):
    os = sys.platform()
    print(os)
Description:
Detect's whether the computer is plugged into AC power

Parameters:
N/A

Returns:
N/A
"""
def detect_power():
    battery = psutil.sensors_battery()
    if(battery is None):
        print("This device does not have a battery. Exiting...")
        sys.exit(1)
    
    while(True):

        while(psutil.sensors_battery().power_plugged):
            print("Running on AC Power")
            time.sleep(1)
    
        send_sms("REPLACE WITH USER PHONE NUMBER")
        open_camera()

        while(not psutil.sensors_battery().power_plugged):
            print("Running on Battery Power")
            play_alarm_mac("mac")
            time.sleep(1)

    

# # Press the green button in the GUI to run the script.
if __name__ == '__main__':
    detect_power()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/