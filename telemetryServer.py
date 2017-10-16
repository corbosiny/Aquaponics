import socket, telemetryClient

class Server():

    def __init__(self, IP= "127.0.0.1", port= 5002, backlogs= 100):
        self.IP = IP
        self.port = port
        self.backlogs = backlogs
    
        self.initializeSocket()

    def initializeSocket(self):
        self.socket = socket.socket()
        self.socket.bind((self.IP, self.port))
        self.socket.listen(self.backlogs)

    def waitForClients(self):
        while True:
            clientSocket, clientIP = self.socket.accept()
            print("Connection made with IP: " + clientIP[0])

            clientHandler = telemetryClient.ClientHandler(clientSocket)
            clientHandler.start()

if __name__ == "__main__":
    server = Server()
    print("Server initalized, now waiting for client connection..")
    server.waitForClients()

    
