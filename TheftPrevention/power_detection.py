import sys
import threading

import psutil
import time


class AC_Adapter:
    """
    desc:
        used to bind functions to adapter plugged and unplugged events.

    Ex:
        See below class
    """
    plugged_listeners = []
    unplugged_listeners = []
    thread = None
    stop = False

    def __init__(self):
        pass

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

######################
#### EXAMPLE CODE ####
######################


def take_photo():
    print("Took photo")


def send_sms():
    print("sent sms")


if __name__ == '__main__':
    adapter = AC_Adapter()
    adapter.addUnpluggedListener(take_photo)
    adapter.addUnpluggedListener(send_sms)

    success = adapter.listen()

    if not success:
        print("Device does not have battery. Exiting...")
        sys.exit(1)

    input()
