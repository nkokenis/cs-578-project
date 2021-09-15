import os
import sys
from typing import final

# Create vairable as final
# Make sure it does not change
COMMANDS: final = {
    "mac": "afplay mixkit-alert-alarm-1005.wav",
    "linux": "aplay mixkit-alert-alarm-1005.wav"
}

def play_alarm(operating_system):
    try:
        # This is dangerous in testing purposes
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