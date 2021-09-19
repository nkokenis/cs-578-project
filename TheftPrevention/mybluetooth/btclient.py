import sys
import threading
import bluetooth


class BTClient:
    def __init__(self, uuid='e4399be5-b392-4490-a842-cc5abce72cb9'):
        service_matches = bluetooth.find_service(uuid=uuid)

        if len(service_matches) == 0:
            raise RuntimeError("Couldn't establish Bluetooth connection.")

        first_match = service_matches[0]
        port = first_match["port"]
        name = first_match["name"]
        host = first_match["host"]

        # Create the client socket
        self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        self.sock.connect((host, port))
        self.connected = True

        self.data_received_listeners = []

        self.recv_thread = threading.Thread(target=self.__recv_data, args=())
        self.recv_thread.start()

    def send_data(self, data):
        self.sock.send(data)

    def __recv_data(self):
        try:
            while self.connected:
                data = self.sock.recv(1024)
                if data == b'':
                    self.connected = False
                for func in self.data_received_listeners:
                    func(data)

            self.sock.close()
        except OSError: # thrown when socket closes
            pass

    def addDataRecvListener(self, func):
        self.data_received_listeners.append(func)

    def removeDataRecvListener(self, func):
        self.data_received_listeners.remove(func)

    def disconnect(self):
        self.connected = False
        try:
            self.sock.close()
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
    print("BT client attempting connection")
    client = BTClient()
    print("BT client established connection")
    client.addDataRecvListener(data_received)

    while True:
        data = input()
        if data == "exit()":
            break
        elif data == "close()":
            client.disconnect()
            break

        client.send_data(data)
