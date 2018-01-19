import paho.mqtt.publish as publish
import string
import random

string.alphanum = '123456789abvcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class ThingSpeakClient():


    def __init__(self, channelID, apiKey, username= "corbosiny24", password= "UT53LDKRW1UWEP9E"):
        self.clientID = ThingSpeakClient.generateClientID()
        self.channelID = channelID
        self.apiKey = apiKey
        self.username = username
        self.password = password
        
    def generateClientID():
        ID = ''
        for i in range(0, 15):
            ID += random.choice(string.alphanum)
        return ID

    def makePost(self, fields, values):
        mqttHost = 'mqtt.thingspeak.com'
        methodOfPosting = 'websockets'
        socketPort = 80

        postTopic = "channels/" + self.channelID + "/publish/" + self.apiKey
        postPayload = self.generatePayLoad(fields, values)

        try:
            publish.single(postTopic, postPayload, hostname= mqttHost, transport= methodOfPosting, port= socketPort, auth= {"username" : self.username, 'password' : self.password})
        except Exception as e:
            print(e)

    def generatePayLoad(self, fields, values):
        payload = str(fields[0]) + "=" + str(values[0])
        for i in range(1, len(fields)):
            payload += '&'
            payload += str(fields[i]) + "=" + str(values[i])
        
        return payload

if __name__ == "__main__":
    testChannelID = "405105"
    testAPIkey = "X7LDFNI8L2IBFITP"

    client = ThingSpeakClient(testChannelID, testAPIkey)
    client.makePost(['field1', 'field2'], [700, 300])
    
