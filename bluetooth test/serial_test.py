import serial

ser = serial.Serial('/dev/rfcomm0',9600)
#ser1 = serial.Serial('/dev/rfcomm1',9600)

while 1:
    input_s = ser.readline()
    print(input_s)
    '''
    input_s1 = ser1.readline()
    print(input_s1)
    '''