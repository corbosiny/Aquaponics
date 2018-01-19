from emailNotifier import EmailNotifier
from thingSpeakClient import ThingSpeakClient
from serialMonitor import SerialMonitor

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
            print(message)
            dataName, dataReading = message.split(',')
            self.updateWebsite(dataName, dataReading)
            self.checkForRedFlags(dataName, dataReading)

    def updateWebsite(self, dataName, dataReading):
        dataFields = [TelemetryManager.dataNames[dataName]]
        dataReadings = [float(dataReading)]
        self.thingSpeakHandler.makePost(dataFields, dataReadings)

    def checkForRedFlags(self, dataName, dataReading):
        if dataName == 'Temperature' and int(dataReading) <= 50:
            message = "Hey {}, \nI am a notification bot, I am in testing mode. A red flag has been raised when reading " + dataName + ". The temperature was reading: {}. Let Corey know if you got this message"
            self.emailHandler.notifyUsers(message, dataReading)
            print('done')            
        

if __name__ == "__main__":

    system = TelemetryManager()
    system.run()
