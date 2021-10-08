import os
import platform

# Create vairable as final
COMMANDS = {
    "darwin": "afplay mixkit-alert-alarm-1005.wav",
    "linux": "aplay mixkit-alert-alarm-1005.wav",
    "windows": "start mixkit-alert-alarm-1005.wav"
}

def play_alarm():
    try:
        print("playing alarm")
        #The below line sets the computer's volume to max, use with caution
        # os.system('osascript -e "set Volume 10"')

        """
        ADDING LOOP HERE DOES NOT ALLOW FOR CTRL+C commands to stop program
        """
        print("System is at max volume")
        os.system(COMMANDS[platform.system().lower()])
        print("Playing Alarm...")
    except KeyboardInterrupt:
        print('Interrupted')
        raise SystemExit