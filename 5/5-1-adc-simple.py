import RPi.GPIO as GPIO
import time
dac = [6,12,5,0,1,7,11,8]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

def decimal2binary(val):
    return [int(el) for el in bin(val)[2:].zfill(8)]
def adc():
    value = 0
    for i in range(8):
        b=1<<(7-i)
        value+=b
        GPIO.output(dac,decimal2binary(value))
        time.sleep(0.01)
        if GPIO.input(comp)==0:
            value-=b
    return value

try:
    while True:
        d = adc()
        if d==0:
            print('Цифровое: {:3d}, Напряжение:{:.2f}B'.format(d,0))
        else:
            v = 3.3*d/255
            print('Цифровое: {:3d}, Напряжение:{:.2f}B'.format(d,v))
except KeyboardInterrupt:
    print('Stop')
finally:
    GPIO.output()(dac,GPIO.LOW)
    GPIO.output(troyka,GPIO.LOW)
    GPIO.cleanup()
