from SMS import sms
from Alarm import play_alarm
from Camera import open_camera
import sys
import psutil
import time
import platform


"""
-> Function: Detect Power
Detect's whether the computer is plugged into AC power
Calls TheftPrevention functions
-> Parameters:
N/A
-> Returns:
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
    
        sms.send_sms("REPLACE WITH USER PHONE NUMBER")
        open_camera()

        while(not psutil.sensors_battery().power_plugged):
            print("Running on Battery Power")
            play_alarm_mac(detect_system())
            time.sleep(1)


"""
-> Function: detect_system
Detects what operating system the program is running on 
-> Parameters:
N/A
-> Returns:
os: String
    Operating System name
"""
def detect_system():
    os = platform.system().lower()
    if os == 'darwin':
        os = 'mac'
    return os
    

# # # Press the green button in the GUI to run the script.
# if __name__ == '__main__':
#     detect_power()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
