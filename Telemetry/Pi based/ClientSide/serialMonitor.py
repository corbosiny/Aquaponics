import serial

class SerialMonitor():

    def __init__(self, comPort, baudRate = 9600):
        self.comPort = comPort
        self.baudRate = baudRate
        self.serialConnection = serial.Serial(comPort, baudRate)

    def displaySerialMonitor(self):
        if self.dataIsAvailable:
            serialMonitorData = self.getLineFromComPort()
            print(serialMonitorData, end= '')
        
    def getIntFromComPort(self):
        serialData = self.getLineFromComPort()
        return int(serialData)

    def getFloatFromComPort(self):
        serialData = self.getLineFromComPort()
        return float(serialData)

    def getLineFromComPort(self):
        line = ''
        lastCharReceived = ''
        while '\n' not in lastCharReceived: #a new line signals the end of a line
            lastCharReceived = self.getCharFromComPort()
            line += lastCharReceived

        return line

    def getCharFromComPort(self):
        try:
            return self.getByteFromComPort().decode('utf-8')
        except:
            return ""
        
    def getByteFromComPort(self):
        return self.serialConnection.read()

    def dataIsAvailable():
        if self.serialConnection.in_waiting > 0:
            return True

    def sendNumToComPort(self, numToSend):
        numAsString = str(numToSend)
        self.sendStringToComPort(numAsString)

    def sendStringToComPort(self, message):
        self.sendBytesToComPort(message.encode('utf-8'))

    def sendBytesToComPort(self, bytesToSend):
        self.serialConnection.write(bytesToSend)


if __name__ == "__main__":
    comPort = "COM21"
    newMonitor = SerialMonitor(comPort)
    while True:
        userInput = input(">>")                     #only sends once command then gets feedback
        newMonitor.sendStringToComPort(userInput)
        newMonitor.displaySerialMonitor()
