from machine import Pin
from dht import *
from time import *
dhtpin=Pin(25,Pin.IN)
mydht=DHT11(dhtpin)

while True:
    mydht.measure()
    temp = mydht.temperature()
    humi = mydht.humidity()
    print(temp)
    print(humi)
    sleep(3)
