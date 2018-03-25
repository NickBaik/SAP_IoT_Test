####################################################################################################
#'''
# Created on 24.07.2017
# This program reads sensor data from a few sensors *humidity, temperature, light) Raspberry PI 3
# and pushes the data into the SAP Cloud Platform IoT Services for cloud foundry
#
# It needs to be run with Python 3 interpreter and the script needs to be
# located at the following path on your Raspberry PI:
# /home/pi/Desktop/GrovePi/Software/Python
# @author: Matthias Allgaier, SAP SE / Martin Ebert, SAP SE
#'''
####################################################################################################

import sys
sys.path.append('home/pi/Dexter/GrovePi/Software/Python')
import requests
import json
import time
import math
import random
import Adafruit_DHT
import RPi.GPIO as GPIO
from Naked.toolshed.shell import muterun_js
from uuid import getnode as get_mac
import socket
import serial

####################################################################################################
#''' please enter your device ID and your sensorID in the variables below

deviceId = 'newDevice'
sensorId = 'newST'

#'''
####################################################################################################

#call node script for converting the certificate from json to pem
response = muterun_js('./converter/converter.js')
if response.exitcode == 0:
    print(response.stdout)
else:
    print(response.stderr)


# find out mac address and hostname
#deviceID = mac
#for i in range (16-len(mac)):
#    deviceID= deviceID + '0'

mac = (hex(get_mac())).lstrip('0x')
host = socket.gethostname()
hostn = int(host[3:])
tenant = 'https://iotae-web-ide2.canary.cp.iot.sap/iot/gateway/rest/measures/'
postAddress = (tenant + deviceId)
factor = 0
port="/dev/ttyUSB0"

print ('MAC:' , mac)
print ('Device ID: ', deviceId)
print ('Sensor ID: ', sensorId)
print ('Hostname:', host)
print ('Posting to:', postAddress)


timeIntervall = 5


'''
GPIOPin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOPin,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
valueLight = 0
input_f = 100
serialFromArduino = serial.Serial(port, 9600)
serialFromArduino.flushInput()
'''

while True:
    
    try:
        '''
        print("")
        print("============================================")
        print("Reading sensor data ...")
  
        # Read dustvalue
        input_s= serialFromArduino.readline()
        input_f=float(input_s)
        print(input_f)
        '''
        input_random1=random.randint(0,100)
        input_random2=random.randint(100,200)
        input_random3=random.randint(200,300)
        print("Random value 1: ",input_random1,"Random value 2: ",input_random2,"Random value 3: ",input_random3)

        
####################################################################################################
# Create http post
#'''
# Create the HTTP POST message and send it to the SAP Internet of Things service.
# The script uses the MAC address in the URL according to your physical device. If the MAC is not
# 16 digits long, it is extended at the end with '0000'

#       Example:
#       ========
#    
#        MAC adress without '-' or ':' b827eb9d3f4c + '0000'
#        '''
####################################################################################################


        data = json.dumps({"capabilityAlternateId":"newCapa", "measures":[[input_random1,input_random2,input_random3]],"sensorAlternateId": sensorId})
        headers = {'content-type': 'application/json'}
        r = requests.post(postAddress,data=data, headers = headers,cert='keyStore.pem', timeout=5)
        responseCode = r.status_code
        print ("==> HTTP Response: %d" %responseCode)
        
        
        # wait timeIntervall [s] before reading the sensor values again
        time.sleep(timeIntervall)
        
    except IOError:
        print ("Error")
       
