import os
from typing import final

# Create vairable as final
COMMANDS: final = {
    "darwin": "afplay mixkit-alert-alarm-1005.wav",
    "linux": "aplay mixkit-alert-alarm-1005.wav",
    "windows": "start C:/mixkit-alert-alarm-1005.wav"
}

def play_alarm(operating_system):
    try:
        #The below line sets the computer's volume to max, use with caution
        #os.system('osascript -e "set Volume 10"')

        """
        ADDING LOOP HERE DOES NOT ALLOW FOR CTRL+C commands to stop program
        """
        print("System is at max volume")
        os.system(COMMANDS[operating_system])
        print("Playing Alarm...")
    except KeyboardInterrupt:
        print('Interrupted')
        raise SystemExit