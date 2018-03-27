from machine import Pin
from dht import DHT11
from time import sleep 

# initialize GPIO
sensor = DHT11(Pin(23))

# read data using pin 14
while True:
    try:
        sensor.measure()
        t = sensor.temperature()
        h = sensor.humidity()
        if isinstance(t, float) and isinstance(h, float):
            msg = (b'{0:3.1f},{1:3.1f}'.format(t, h))
            #client.publish(TOPIC, msg)
            print(msg)
        else:
            print('Invalid sensor readings.')
    except OSError:
        print('Failed to read sensor.')
    sleep(4)
