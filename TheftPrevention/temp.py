import sys
import psutil
import time
from SMS import send_sms


def main():
    battery = psutil.sensors_battery()
    if(battery is None):
        print("This device does not have a battery. Exiting...")
        sys.exit(1)

    while(True):

        while(psutil.sensors_battery().power_plugged):
            print("Running on AC Power")
            time.sleep(1)
    
        send_sms()

        while(not psutil.sensors_battery().power_plugged):
            print("Running on Battery Power")
            time.sleep(1)

    

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
