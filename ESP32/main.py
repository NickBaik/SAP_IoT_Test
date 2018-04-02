import network
from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import *
import random
from hcsr04 import HCSR04

dhtpin=machine.Pin(25,machine.Pin.IN)
mydht=DHT11(dhtpin)

sensor = HCSR04(trigger_pin=16, echo_pin =0, echo_timeout_us=10000)
dustDigital = machine.Pin(32, machine.Pin.OUT) # D6 Pin digital out

delayTime=2.8
delayTime2=0.04
offTime=0.9680
distance = 0

def blink():
    led14 = machine.Pin(14, machine.Pin.OUT)
    led14.value(1)
    sleep(0.5)
    led14.value(0)
    sleep(0.5)
    
def ultra():
    try:
        distance_float = sensor.distance_cm()
        global distance
        distance = int(distance_float)
        #print('Distance = ',distance, 'cm')
        sleep(1)
    except OSError as ex:
        print('ERROR getting distance:', ex)
        
def goBeep():
    if 1:
        p17 = machine.Pin(17)
        pwm17 = machine.PWM(p17)
        pwm17.duty(100)


def stopBeep():
    if 1:
        p17 = machine.Pin(17)
        pwm17 = machine.PWM(p17)
        pwm17.duty(0)
        

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("Baek","82388238")

sleep(5)

SERVER = '192.168.43.251'
CLIENT_ID = 'ESP32_DHT11_Sensor'
TOPIC = b'listenPi'

client = MQTTClient(CLIENT_ID, SERVER)
client.connect()
# blink 2 times
blink()
blink()

while True:
    try:        
        mydht.measure()
        temp = mydht.temperature()-5
        humi = mydht.humidity()
        print('temp = ', temp)
        print('humi = ', humi)
        print('distance = ', distance)
        
        if (distance > 40):
            goBeep()
        elif (distance < 40):
            stopBeep()
        
        sleep(1)
        ultra()
        
        
        
        tempmsg = str(temp)
        humimsg = str(humi)
        distmsg = str(distance)
        
        msg = "d1 = temp: " + tempmsg + " humi : " + humimsg + " dist = " +distmsg + " "
        client.publish(TOPIC, msg)
        blink()
        blink()
        print(msg)
    except OSError:
        print('Failed to read sensor')
	
	