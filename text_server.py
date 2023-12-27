import socket
import threading

class RCServer:
    def __init__(self):
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket = None
        self.server_socket.bind(("localhost", 5555))
        self.server_socket.listen(2)

    def run_server(self):
        # accept connections:
        while True:
            self.client_socket, addr = self.server_socket.accept()
            self.clients.append(self.client_socket)
            # allow for the multiple clients to send data:
            client_handler = threading.Thread(target=self.handle_client, args=(self.client_socket,))
            client_handler.start()

    def handle_client(self, socket):
        while True:
            try:
                # receive data
                data = socket.recv(1024)
                if data == b'QUIT':
                    print(f"Client is quitting. Closing the server.")
                    break
                # send data back to all clients
                for client in self.clients:
                    client.send(data)
            except (ConnectionAbortedError, ConnectionResetError):
                #self.clients.remove(self.client_socket)
                break
        print("CLOSE SOCKET server")
        self.client_socket.close()
        self.server_socket.close()

if __name__ == "__main__":
    server = RCServer()
    server.run_server()