from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import DHT11
import random

SERVER = '192.168.1.10'
#PORT = 61618
CLIENT_ID = 'ESP8266_1'
TOPIC = 'measures/edge_test2'


print(1)
client = MQTTClient(CLIENT_ID, SERVER, port=61618)
client.connect()
led = machine.Pin(2, machine.Pin.OUT)
print("connected")

while True:
    try:
	input_random1=random.randint(100,200)
	msg = '''{"capabilityAlternateId": "edge_capa","sensorTypeAlternateId": 3363,
"sensorAlternatedId":"edge_sensor",
"measures": [["%d"]]}''' %input_random1
	client.publish(TOPIC, msg)
	print(msg)
	led.off() # Board LED on
    except OSError:
        print('Failed to read sensor. or the broker doesn not work')
    sleep(2)
    print(4)
    led.on()
    sleep(2)

