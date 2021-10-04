import sys
import time
import platform
import psutil
import threading
from cache import access_cache
from Webcam import capture
from SMS import send_sms as send
#from Alarm import play_alarm as alarm

class AC_Adapter:
    """
    desc:
        used to bind functions to adapter plugged and unplugged events.

    Ex:
        See below class
    """
    def __init__(self):
        self.plugged_listeners = []
        self.unplugged_listeners = []
        self.thread = None
        self.stop = False
        

    def addUnpluggedListener(self, func):
        self.unplugged_listeners.append(func)

    def removeUnpluggedListener(self, func):
        self.unplugged_listeners.remove(func)

    def addPluggedListener(self, func):
        self.plugged_listeners.append(func)

    def removePluggedListener(self, func):
        self.plugged_listeners.remove(func)


    def listen(self):
        """
            desc: Begins AC adapter plug detection
            return: true if device has a battery, false otherwise
        """
        battery = psutil.sensors_battery()
        if battery is None:
            # This device does not have a battery.
            return False

        self.stop = False
        self.thread = threading.Thread(target=self.__listen, args=())
        self.thread.start()

        return True
        

    def stop_listening(self):
        """
        desc: Ends AC adapter plug detection
        """
        self.stop = True
    
    
    def __listen(self):
        """
        desc: Private helper function for listen.
            The function that runs in separate thread.
        """
        while True:
            while psutil.sensors_battery().power_plugged:
                # Running on AC Power
                if self.stop:
                    return
                time.sleep(1)

            for func in self.unplugged_listeners:
                func()

            while not psutil.sensors_battery().power_plugged:
                # Running on Battery Power
                if self.stop:
                    return
                time.sleep(1)

            for func in self.plugged_listeners:
                func()


#######################
#### Functionality ####
#######################
def detect_os():
    return platform.system().lower()
'''
def play_alarm():
    alarm(detect_os())
'''
def take_photo():
    capture()

def send_sms():
    send(access_cache("phone_number"))


###############
## Test File ##
###############
if __name__ == '__main__':
    adapter = AC_Adapter()
    adapter.addUnpluggedListener(play_alarm)
    adapter.addUnpluggedListener(take_photo)
    adapter.addUnpluggedListener(send_sms)

    success = adapter.listen()

    if not success:
        print("Device does not have battery. Exiting...")
        sys.exit(1)