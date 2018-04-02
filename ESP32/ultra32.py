from hcsr04 import HCSR04
import time

sensor = HCSR04(trigger_pin=16, echo_pin =0, echo_timeout_us=10000)

while 1:
    try:
        distance = sensor.distance_cm()
        print('Distance : ',distance, 'cm')
        time.sleep(1)
    except OSError as ex:
        print('ERROR getting distance:', ex)