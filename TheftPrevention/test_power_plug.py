import sys

import psutil
import time

def main():
    battery = psutil.sensors_battery()
    if(battery is None):
        print("This device does not have a battery. Exiting...")
        sys.exit(1)

    while(True):
        battery = psutil.sensors_battery()

        print(battery.power_plugged)
        time.sleep(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
