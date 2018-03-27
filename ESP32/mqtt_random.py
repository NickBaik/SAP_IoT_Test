from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT11
import random

SERVER = '192.168.43.251'
CLIENT_ID = 'ESP32_DHT11_Sensor'
TOPIC = b'temp_humidity'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

while True:
    try:
	input_random1=random.randint(0,100)
	msg = str(input_random1)
	client.publish(TOPIC, msg)
	print(msg)
    except OSError:
        print('Failed to read sensor.')
    sleep(4)

