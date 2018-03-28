import machine
from time import sleep
from dht import *
#adc = machine.ADC(0) # enable analog 0 ADC reading
adc = machine.ADC(machine.Pin(34))
dhtpin=machine.Pin(25,machine.Pin.IN)
mydht=DHT11(dhtpin)

#print('3')
dustDigital = machine.Pin(32, machine.Pin.OUT) # D6 Pin digital out

delayTime=2.8
delayTime2=0.04
offTime=0.9680

while True:
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





