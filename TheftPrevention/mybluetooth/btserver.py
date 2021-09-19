import sys
import threading

import bluetooth


class BTServer:
    #uuid = 'e4399be5-b392-4490-a842-cc5abce72cb9'
    uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    def __init__(self, uuid="94f39d29-7d6d-437d-973b-fba39e49d4ee"):
        server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]

        bluetooth.advertise_service(server_sock, "AntiTheftServer", service_id=uuid,
                                    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

        self.client_sock, self.client_info = server_sock.accept()
        self.connected = True

        self.data_received_listeners = []

        self.recv_thread = threading.Thread(target=self.__recv_data, args=())
        self.recv_thread.start()

    def send_data(self, data):
        self.client_sock.send(data)

    def __recv_data(self):
        while self.connected:
            data = self.client_sock.recv(1024)
            if data == b'':
                self.connected = False
            for func in self.data_received_listeners:
                func(data)

        self.client_sock.close()

    def addDataRecvListener(self, func):
        self.data_received_listeners.append(func)

    def removeDataRecvListener(self, func):
        self.data_received_listeners.remove(func)

    def disconnect(self):
        self.connected = False

def data_received(data):
    print(data)

if __name__ == '__main__':
    print("BT server waiting for client")
    server = BTServer()
    print("BT server established connection")
    server.addDataRecvListener(data_received)

    input()