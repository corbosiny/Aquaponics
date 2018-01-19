from emailNotifier import EmailNotifier
from thingSpeakClient import ThingSpeakClient
from serialMonitor import SerialMonitor

import time

testChannelID = "405105"
testAPIkey = "X7LDFNI8L2IBFITP"

class TelemetryManager():

    dataNames = {"Moisture" : 'field1', 'Temperature' : 'field2'}
    dataThresholds = {}

    def __init__(self, COM= "COM19"):
        self.serialConnection = SerialMonitor(COM)
        self.emailHandler = EmailNotifier('coreyohulse@gmail.com', 'kenshin247')
        self.thingSpeakHandler = ThingSpeakClient(testChannelID, testAPIkey)
        

    def run(self):
        while True:
            message = self.serialConnection.getLineFromComPort()
            dataName, dataReading = message.split(',')
            self.updateDataFile(dataName, dataReading)
            self.updateWebsite(dataName, dataReading)
            #self.checkForRedFlags(dataName, dataReading)

    def updateWebsite(self, dataName, dataReading):
        dataFields = [TelemetryManager.dataNames[dataName]]
        dataReadings = [float(dataReading)]
        self.thingSpeakHandler.makePost(dataFields, dataReadings)

    def checkForRedFlags(self, dataName, dataReading):
        if dataName == 'Temperature' and float(dataReading) <= 50:
            message = "Hey {}, \nI am a notification bot, I am in testing mode. A red flag has been raised when reading " + dataName + ". The temperature was reading: {}. Let Corey know if you got this message"
            self.emailHandler.notifyUsers(message, dataReading)        


    def updateDataFile(self, dataname, data):
        date = time.strftime("%d-%m-%Y")
        timeStamp = time.strftime("%H:%M:%S")
        self.writeToFileWhenOpen(date, timeStamp, dataname, data)

    def writeToFileWhenOpen(self, date, timeStamp, dataname, data):
        while True:
            try:
                with open(dataname + "DataFile-" + date + '.txt', "a") as file:
                    file.write(str(timeStamp) + "," + str(data));
                break
            except:
                pass

if __name__ == "__main__":

    system = TelemetryManager()
    system.run()
