import network
from time import sleep
from umqtt.simple import MQTTClient
import machine
from dht import DHT11
import random

def sub_cb(topic, msg):
    print((topic, msg))
    blink()
    blink()
    #print(str(msg))
    if(str(msg) == 'b\'ON\''): # \' represent '
        print('Motor on')
        p17 = machine.Pin(17)
        pwm17 = machine.PWM(p17)
        pwm17.duty(1022)
        pwm14.duty(1022)
    elif(str(msg) == 'b\'OFF\''):
        print('Motor off')
        p17 = machine.Pin(17)
        pwm17 = machine.PWM(p17)
        pwm17.duty(500)
        pwm14.duty(0)
    
    
    
def blink():
    led14 = machine.Pin(14, machine.Pin.OUT)
    led14.value(1)
    sleep(0.5)
    led14.value(0)
    sleep(0.5)
    
    
def motorSetup():
    p17 = machine.Pin(17)
    p16 = machine.Pin(16)
    pwm17 = machine.PWM(p17)
    pwm16 = machine.PWM(p16)
    pwm17.freq(500)
    pwm16.freq(500)
    pwm17.duty(500)
    pwm16.duty(500)
    
def buzzerSetup():
    p14 = machine.Pin(14)
    pwm14 = machine.PWM(p14)
    pwm14.freq(500)
    pwm14.duty(0)
    
    

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
motorSetup()
buzzerSetup()
print('allset')

#blink 3times
blink()
blink()

#


while True:
    try:
        while 1:
            #print('wait msg1')
            client.subscribe(b"motorDevice1")
            client.wait_msg()
            #print('wait msg2')
    except OSError:
        print('Failed to read sensor.')
        sleep(3)
