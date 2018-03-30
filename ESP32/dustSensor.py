import machine
from time import sleep
adc = machine.ADC(0) # enable analog 0 ADC reading
dustDigital = machine.Pin(12, machine.Pin.OUT) # D6 Pin digital out

delayTime=2.8
delayTime2=0.04
offTime=0.9680

while True:
         dustDigital.off()
         sleep(delayTime/ 1000)

         dustVal = adc.read()
         sleep(delayTime2/ 1000)

         dustDigital.on()
         sleep(offTime / 1000)

         sleep(3);

         dustDensity = (0.17*(dustVal*0.0049)-0.1)*(1000)+135; #135 is for sensor error
         print('Dust density(ug/m3) = ', dustDensity)




