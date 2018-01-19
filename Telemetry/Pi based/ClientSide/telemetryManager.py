from emailNotifier import EmailNotifier
from thingSpeakClient import ThingSpeakClient
from serialMonitor import SerialMonitor

import time

testChannelID = "405105"
testAPIkey = "X7LDFNI8L2IBFITP"

class TelemetryManager():

    dataNames = {"Moisture" : 'field1', 'Temperature' : 'field2'}
    dataThresholds = {"Moisture" : [], 'Temperature' : []}

    LOWER_THRESHOLD_WARNING = "Hey {},\n\nAquaponics sensor bot here, we have a lower threshold warning for {} because of a low reading of {}"
    UPPER_THRESHOLD_WARNING = "Hey {},\n\nAquaponics sensor bot here, we have a upper threshold warning for {} because of a high reading of {}

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
        thresholds = dataThresholds[dataName]

        message = None
        if dataReading < dataThresholds[0]:
            message = TelemetryManager.LOWER_THRESHOLD_WARNING
        elif dataReading > dataThresholds[1]
            message = TelemetryManager.UPPER_THRESHOLD_WARNING

        if message != None:
            self.emailNotifier.notifyUsers(message, dataName, dataReading)

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
