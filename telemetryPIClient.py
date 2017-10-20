import socket, time, threading
from serialMonitor import SerialMonitor

class Client(threading.Thread):

    def __init__(self, IP= "127.0.0.1", port= 80, COM= "/dev/ttyACM0", baud= 9600, timeOut = 10):
        self.IP = IP
        self.port = port
        self.COM = COM
        self.baud = baud
        self.timeOut = timeOut
        
        self.initializeSocket()
        self.attemptConnectionWithServer()
        self.initializeSerialMonitor()
        super(Client, self).__init__()
        
    def initializeSocket(self):
        self.socket = socket.socket()
        self.socket.settimeout(self.timeOut)

    def attemptConnectionWithServer(self):
        try:
            self.socket.connect((self.IP, self.port))
            print("Connection established to server")
        except:
            print("Socket initialization failed\n")
            
    def initializeSerialMonitor(self):
        self.serialMonitor = SerialMonitor(self.COM, self.baud)

    def sendDataToServer(self, dataToSend):
        try:
            bytesToSend = dataToSend.encode("utf-8")
            self.socket.send(bytesToSend)
        except:
            print("Problem with connection, attempting reinitialization..")
            self.attemptConnectionWithServer()

    def updateDataFile(self, data):
        date = time.strftime("%d-%m-%Y")
        timeStamp = time.strftime("%H:%M:%S")
        self.writeToFileWhenOpen(date, timeStamp, data)

    def writeToFileWhenOpen(self, date, timeStamp, data):
        while True:
            try:
                with open("DataFile-" + date, "a") as file:
                        file.write(str(timeStamp) + ", " + str(data));
                break
            except:
                pass
        
    def run(self):
        while True:
            dataToSend = self.serialMonitor.getLineFromComPort()
            self.sendDataToServer(dataToSend)
            self.updateDataFile(dataToSend)
            
if __name__ == "__main__":
    IPaddr = "192.168.1.70"
    port = 5002
    testClient = Client(IP= IPaddr, port= port)
    testClient.start()
