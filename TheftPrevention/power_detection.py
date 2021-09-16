from TheftPrevention.Camera import open_camera
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
        battery = psutil.sensors_battery()

        while(psutil.sensors_battery().power_plugged):
            print("Running on AC Power")
            time.sleep(1)
    
        #send_sms('user phone number')
        open_camera()

        while(not psutil.sensors_battery().power_plugged):
            print("Running on Battery Power")
            time.sleep(1)