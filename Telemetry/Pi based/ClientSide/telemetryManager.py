from clientToWebsiteSerber import Client
from serialMonitor import SerialMonitor

class TelemetryManager():

    def __init__(self, server= "127.0.0.1", serverPort= 80, filePort= 5003, COM= "/dev/ttyACM0"):
        self.webSiteClient = Client(IP= server, port= serverPort, COM= COM)
        self.webSiteClient.start()

        self.initializeServer()

    def initializeServer(self):
        self.server = socket.socket()
        self.server.bind(("0.0.0.0", self.filePort))
        self.server.listen(5)

    def run(self):
        while True:
            client, clientIP = self.server.accept()
            fileHandler = TelemetryFileHandler(client)
            fileHandler.start()

if __name__ == "__main__":
    websiteServer = ""
    serverPort = 5002
    filePort = 5003
    system = TelemetryManager(server= websiteServer, serverPort= serverPort, filePort= filePort)
    system.run()
