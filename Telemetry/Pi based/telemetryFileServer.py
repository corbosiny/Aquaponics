import threading, socket

class TelemetryFileHandler(threading.Thread):

    def __init__(self, port= 5003, allowedBackLogs= 5):
        self.port = port
        self.allowedBackLogs= allowedBackLogs
        self.initializeServer()

        super(TelemetryFileHandler, self).__init__()

    def initializeServer(self):
        self.socket.socket()
        self.socket.bind(("0.0.0.0", self.port))
        self.socket.listen(self.allowedBackLogs)

    def receiveCommand(self):
        command = self.
