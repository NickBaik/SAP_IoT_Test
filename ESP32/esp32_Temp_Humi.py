from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT11

SERVER = '192.168.43.251'
CLIENT_ID = 'ESP32_DHT11_Sensor'
TOPIC = b'temp_humidity'

cleint = MQTTClient(CLIENT_ID, SERVER)
client.connect()

sensor = DHT11(Pin(23))

while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            client.publish(TOPIC, msg)
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(4)

