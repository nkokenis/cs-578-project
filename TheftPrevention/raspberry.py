from mybluetooth import btserver
import SMS

user_phone_number = None


def bt_data_recieved(tuple_data):
    global user_phone_number

    key = tuple_data[0]
    data = tuple_data[1]

    if key == "#":
        user_phone_number = data
        print("received user phone#:", user_phone_number)
    if key == "sms":
        if user_phone_number is not None:
            SMS.send_sms(user_phone_number)


def laptop_disconnected():
    global user_phone_number
    print("laptop disconnected")
    if user_phone_number is not None:
        SMS.send_sms(user_phone_number)


if __name__ == '__main__':
    bluetooth_server = btserver.BTServer()
    bluetooth_server.add_disconnect_listener(laptop_disconnected)
    bluetooth_server.add_data_recv_listener(bt_data_recieved)
    print("Starting bluetooth server")
    bluetooth_server.start()
    bluetooth_server.wait_for_connection()
    print("Bluetooth client connected")