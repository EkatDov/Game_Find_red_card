import socket
import threading

class RCClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("localhost", 5555))

    def run_client(self):
        receive_thread = threading.Thread(target=self.receive_messages, args=(self.client_socket,))
        receive_thread.start()
        self.send_message()

    def receive_messages(self, socket):
        while True:
            try:
                response = socket.recv(1024)
            except OSError:
                print(f"Client is disconnected")
                break
            else:
                print(response.decode('utf-8'))

    def send_message(self):
        while True:
            message = input()
            # exit the client
            if message.strip() == "q":
                self.client_socket.sendall("QUIT".encode('utf-8'))
                break
            else:
                # send the message
                self.client_socket.sendall(message.encode('utf-8'))

if __name__ == "__main__":
    c = RCClient()
    c.run_client()