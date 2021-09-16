import os
import sys
from typing import final

# Create vairable as final
COMMANDS: final = {
    "mac": "afplay mixkit-alert-alarm-1005.wav",
    "linux": "aplay mixkit-alert-alarm-1005.wav"
}

def play_alarm(operating_system):
    try:
        #The below line sets the computer's volume to max, use with caution
        #os.system('osascript -e "set Volume 10"')
        print("System is at max volume")
        while True:
            os.system(COMMANDS[operating_system])
            print("Playing Alarm...")
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)