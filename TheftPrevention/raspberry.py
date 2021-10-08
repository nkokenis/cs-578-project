import ctypes
import threading

from mybluetooth import btserver
from datetime import datetime
from queue import Queue
import signal
import sys
import cv2 # pip install opencv-python
import SMS
import Alarm
import time

bluetooth_server = None
user_phone_number = None
enabled = False

img_buffer_size = 10
img_buffer = Queue(img_buffer_size)


def signal_handler(sig, frame):
    bluetooth_server.shutdown()
    sys.exit(1)


def save_images():
    global img_buffer
    i = 1
    while not img_buffer.empty():
        img = img_buffer.get()
        file_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S.png')+"_"+str(i)  # Timestamp
        cv2.imwrite(file_name, img)
        i = i + 1


def bt_data_received(tuple_data):
    global user_phone_number, enabled, img_buffer

    key = tuple_data[0]
    data = tuple_data[1]

    if key == "img":
        if img_buffer.full():
            img_buffer.get()
        img_buffer.put()
    if key == "#":
        user_phone_number = data
        print("received user phone#:", user_phone_number)
    elif key == "en":
        enabled = True
        print("system enabled")
    elif key == "dis":
        enabled = False
        print("system disabled")
    elif key == "sms":
        if user_phone_number is not None:
            SMS.send_sms(user_phone_number)


def laptop_disconnected():
    global user_phone_number, enabled

    print("laptop disconnected")
    if enabled and user_phone_number is not None:
        print("sending sms.")
        SMS.send_sms(user_phone_number)
        Alarm.play_alarm()
        save_images()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    #time.sleep(10)
    bluetooth_server = btserver.BTServer()
    bluetooth_server.add_connect_listener(lambda: print("client connected."))
    bluetooth_server.add_disconnect_listener(laptop_disconnected)
    bluetooth_server.add_data_recv_listener(bt_data_received)
    print("Starting bluetooth server")
    bluetooth_server.start()

    # don't let thread finish. Or else SIGINT handler wont work
    while True:
        time.sleep(50)
