from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import DHT11
import random

SERVER = '192.168.43.251'
CLIENT_ID = 'ESP8266_DHT11_Sensor'
TOPIC = b'temp_humidity'


print(1)
client = MQTTClient(CLIENT_ID, SERVER)
client.connect()
led = machine.Pin(2, machine.Pin.OUT)
print(2)

while True:
    try:
	input_random1=random.randint(100,200)
	print(3)
	msg = str(input_random1)
	client.publish(TOPIC, msg)
	print(msg)
	led.off() # Board LED on
    except OSError:
        print('Failed to read sensor.')
    sleep(2)
    print(4)
    led.on()
    sleep(2)

