import machine
from time import sleep
#adc = machine.ADC(0) # enable analog 0 ADC reading


if True:
    p23 = machine.Pin(23)
    p32 = machine.Pin(32)
    pwm23 = machine.PWM(p23)
    pwm32 = machine.PWM(p32)
    
    
    #pwm23.freq(50)
    pwm23.duty(1023)
    
    
    sleep(5)
    
    #off
    pwm23.duty(0)
    #pwm32.duty(1023)
    
    sleep(5)
    
    pwm23.duty(512)
    
    
         
