import network
from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import *
import random

dhtpin=machine.Pin(25,machine.Pin.IN)
mydht=DHT11(dhtpin)

adc = machine.ADC(machine.Pin(34))
dustDigital = machine.Pin(32, machine.Pin.OUT) # D6 Pin digital out

delayTime=2.8
delayTime2=0.04
offTime=0.9680

def blink():
    led14 = machine.Pin(14, machine.Pin.OUT)
    led14.value(1)
    sleep(0.5)
    led14.value(0)
    sleep(0.5)

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Baek","82388238")

sleep(5)

SERVER = '192.168.43.251'
CLIENT_ID = 'ESP32_DHT11_Sensor'
TOPIC = b'listenPi'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()

while True:
    try:        
        dustDigital.value(0)
        sleep(delayTime/ 1000)
        #print('1')

        dustVal = adc.read()
        sleep(delayTime2/ 1000)
        #print('2')

        dustDigital.value(1)
        sleep(offTime / 1000)

        sleep(3);

        dustDensity = (0.17*(dustVal*0.0049)-0.1)*(1000)+135; #135 is for sensor error
        print('Dust density(ug/m3) = ', dustDensity)
        mydht.measure()
        temp = mydht.temperature()-5
        humi = mydht.humidity()
        print('temp = ', temp)
        print('humi = ', humi)
        sleep(3)
        
        tempmsg = str(temp)
        humimsg = str(humi)
        dustmsg = str(dustDensity)
        
        msg = "d1 = temp: " + tempmsg + " humi : " + humimsg + " dust : " +dustmsg + " "
        client.publish(TOPIC, msg)
        print(msg)
    except OSError:
        print('Failed to read sensor')
	
	