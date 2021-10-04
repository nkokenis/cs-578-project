import sys
import threading
import bluetooth # pip pybluez22


class BTServer:
    def __init__(self, uuid='e4399be5-b392-4490-a842-cc5abce72cb9'):
        self.server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.server_sock.bind(("", bluetooth.PORT_ANY))
        self.server_sock.listen(1)

        port = self.server_sock.getsockname()[1]

        bluetooth.advertise_service(self.server_sock, "AntiTheftServer", service_id=uuid,
                                    service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                                    profiles=[bluetooth.SERIAL_PORT_PROFILE],
                                    # protocols=[bluetooth.OBEX_UUID]
                                    )

        self.client_sock, self.client_info = self.server_sock.accept()
        self.connected = True

        self.data_received_listeners = []

        self.recv_thread = threading.Thread(target=self.__recv_data, args=())
        self.recv_thread.start()

    def send_data(self, data):
        self.client_sock.send(data)

    def __recv_data(self):
        try:
            while self.connected:
                data = self.client_sock.recv(1024)
                if data == b'':
                    self.connected = False
                for func in self.data_received_listeners:
                    func(data)

            self.client_sock.close()
        except OSError:
            pass

    def addDataRecvListener(self, func):
        self.data_received_listeners.append(func)

    def removeDataRecvListener(self, func):
        self.data_received_listeners.remove(func)

    def disconnect(self):
        self.connected = False
        try:
            self.client_sock.close()
            self.server_sock.close()
        except OSError:
            pass
        
    def isConnected(self):
        return self.connected


######################
#### EXAMPLE CODE ####
######################

def data_received(data):
    print(data)


if __name__ == '__main__':
    print("BT server waiting for client")
    server = BTServer()
    print("BT server established connection")
    server.addDataRecvListener(data_received)

    while True:
        data = input()
        if data == "exit()":
            break
        elif data == "close()":
            server.disconnect()
            break

        server.send_data(data)