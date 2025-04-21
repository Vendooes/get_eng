import RPi.GPIO as GPIO
import time
dac = [6,12,5,0,1,7,11,8]
leds = [9,10,22,27,17,4,3,2]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
GPIO.setup(leds,GPIO.OUT)

def decimal2binary(val):
    return [int(el) for el in bin(val)[2:].zfill(8)]
def adc():
    value = 0
    for i in range(8):
        value+=2**(7-i)
        GPIO.output(dac,decimal2binary(value))
        time.sleep(0.001)
        if GPIO.input(comp)==1:
            value-=2**(7-i)
    return value

try:
    while True:
        d = adc()

        v = 3.3*d/256
        if d<57:
            GPIO.output(leds,[0,0,0,0,0,0,0,1])
        elif d<85:
            GPIO.output(leds,[0,0,0,0,0,0,1,1])
        elif d<114:
            GPIO.output(leds,[0,0,0,0,0,1,1,1])
        elif d<142:
            GPIO.output(leds,[0,0,0,0,1,1,1,1])
        elif d<171:
            GPIO.output(leds,[0,0,0,1,1,1,1,1])
        elif d<199:
            GPIO.output(leds,[0,0,1,1,1,1,1,1])
        elif d<228:
            GPIO.output(leds,[0,1,1,1,1,1,1,1])
        else:
            GPIO.output(leds,[1,1,1,1,1,1,1,1])
        print('Цифровое: {:3d}, Напряжение:{:.2f}B'.format(d,v))
except KeyboardInterrupt:
    print('Stop')
finally:
    GPIO.output()(dac,GPIO.LOW)
    GPIO.output(troyka,GPIO.LOW)
    GPIO.cleanup()
