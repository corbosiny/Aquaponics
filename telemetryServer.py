import socket, clientHandler, subprocess

class Server():

    def __init__(self, IP= "127.0.0.1", port= 5002, backlogs= 100):
        self.IP = IP
        self.port = port
        self.backlogs = backlogs
        print("Server Hostname: " + socket.gethostname())
        print("IP: ", Server.getIPaddress())
        print("Port:", port)
        self.initializeSocket()
        print("Server initalized, now waiting for client connection..")
        print("_" * 50)

    def initializeSocket(self):
        self.socket = socket.socket()
        self.socket.bind((self.IP, self.port))
        self.socket.listen(self.backlogs)

    def waitForClients(self):
        while True:
            clientSocket, clientIP = self.socket.accept()
            print(">> Connection made with IP: " + clientIP[0])

            clientHandler = telemetryClient.ClientHandler(clientSocket)
            clientHandler.start()

    def getIPaddress():
        subroutineCall = subprocess.Popen("hostname -I", shell= True, stdout= subprocess.PIPE, stderr= subprocess.PIPE)
        return (subroutineCall.stdout.read() + subroutineCall.stderr.read()).decode("utf-8").strip()

if __name__ == "__main__":
    server = Server(IP= "0.0.0.0")
    server.waitForClients()

    
