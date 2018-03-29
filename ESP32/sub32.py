import network
from time import sleep
from umqtt.simple import MQTTClient
from machine import Pin
from dht import DHT11
import random

def sub_cb(topic, msg):
    print((topic, msg))

print('start')
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Baek","82388238")
print('connected1')
sleep(5)

SERVER = '192.168.43.251'
CLIENT_ID = 'motor1'
TOPIC = b'motorDevice1'

client = MQTTClient(CLIENT_ID, SERVER)
print('test')
client.connect()
client.set_callback(sub_cb)
print('allset')



while True:
    try:
        while 1:
            #print('wait msg1')
            client.subscribe(b"motorDevice1")
            client.wait_msg()
            #print('wait msg2')
    except OSError:
        print('Failed to read sensor.')
        sleep(4)
