import threading, socket

class ClientHandler(threading.Thread):

    def __init__(self, clientSocket):
        self.clientSocket = clientSocket
        super(ClientHandler, self).__init__()
        
    def run(self):
        while True:
            data = self.clientSocket.recv(1024).decode("utf-8")
            print(data)

if __name__ == "__main__":
    server = socket.socket()
    server.bind(("0.0.0.0", 5002))
    server.listen(1)
    print("Server Hostname: " + socket.gethostname())
    print("Waiting for clients...")
    
    while True:
        client, clientIP = server.accept()
        clientHandler = ClientHandler(client)
        clientHandler.start()
