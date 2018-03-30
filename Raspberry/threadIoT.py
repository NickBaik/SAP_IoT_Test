import threading
import sys
sys.path.append('home/pi/Dexter/GrovePi/Software/Python')
import requests
import json
import time
import math
import random
#import Adafruit_DHT
import RPi.GPIO as GPIO
from Naked.toolshed.shell import muterun_js
from uuid import getnode as get_mac
import socket
import serial
import paho.mqtt.client as mqtt

#''' please enter your device ID and your sensorID in the variables below

deviceId = 'newDevice'
sensorId = 'newST'

#'''

#call node script for converting the certificate from json to pem
response = muterun_js('./converter/converter.js')
if response.exitcode == 0:
    print(response.stdout)
else:
    print(response.stderr)
#'''

#''' IoT setting
mac = (hex(get_mac())).lstrip('0x')
host = socket.gethostname()
#hostn = int(host[3:])
tenant = 'https://iotae-web-ide2.canary.cp.iot.sap/iot/gateway/rest/measures/'
postAddress = (tenant + deviceId)
factor = 0
port="/dev/ttyUSB0"
timeIntervall = 5
#'''

#''' callback fires when connected to MQTT broker
def on_connect(client, userdata, flag, rc):
         print('Connected with result code {0}'.format(rc))
         #SUbscribe (or renew if reconnect)
         client.subscribe('temp_humidity')

def on_message(client, userdata, msg):
         print(msg.topic+" "+str(msg.payload))
         
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)
#'''



print ('MAC:' , mac)
print ('Device ID: ', deviceId)
print ('Sensor ID: ', sensorId)
print ('Hostname:', host)
print ('Posting to:', postAddress)

class IoT4_0(threading.Thread):
         def run(self):
                  print('MAC:' , mac)
                  print ('Device ID: ', deviceId)
                  print ('Sensor ID: ', sensorId)
                  print ('Hostname:', host)
                  print ('Posting to:', postAddress)
                  while True:
    
                           try:
                                    input_random1=random.randint(0,100)
                                    input_random2=random.randint(100,200)
                                    input_random3=random.randint(200,300)
                                    print("Random value 1: ",input_random1,"Random value 2: ",input_random2,"Random value 3: ",input_random3)

                                    data = json.dumps({"capabilityAlternateId":"newCapa", "measures":[[input_random1,input_random2,input_random3]],"sensorAlternateId": sensorId})
                                    headers = {'content-type': 'application/json'}
                                    r = requests.post(postAddress,data=data, headers = headers,cert='keyStore.pem', timeout=5)
                                    responseCode = r.status_code
                                    print ("==> HTTP Response: %d" %responseCode)
                                    
                                    time.sleep(timeIntervall)
                           except IOError:
                                    print ("Error")
class mqtt(threading.Thread):
         def run(self):
                  client.loop_forever()

                                    
send = IoT4_0()
receive =mqtt()

send.start()
receive.start()
