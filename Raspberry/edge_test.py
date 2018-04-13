from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import DHT11
import random

SERVER = '192.168.1.10'
CLIENT_ID = 'edge_test'
TOPIC = 'measures/edge_test2'


print(1)
client = MQTTClient(CLIENT_ID, SERVER, 61618)
client.connect()
led = machine.Pin(2, machine.Pin.OUT)
print(2)

while True:
    try:
	input_random1=random.randint(100,200)
	print(3)
	msg = '{"sensorTypeAlternatedId":3363,"capabilityAlternatedId":"edge_capa","sensorAlternateId":"edge_sensor","measures":"[[123]]}'
	client.publish(TOPIC, msg)
	print(msg)
	led.off() # Board LED on
    except OSError:
        print('Failed to read sensor.')
    sleep(2)
    print(4)
    led.on()
    sleep(2)

