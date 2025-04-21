import RPi.GPIO as GPIO
import time
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(val):
    return [int(el) for el in bin(val)[2:].zfill(8)]

try:
    period = float(input())
    a=0
    while True:
        while a<=254:
            GPIO.output(dac,decimal2binary(a))
            a+=1
            time.sleep(((period/2)/254))
        while a>=1:
            GPIO.output(dac,decimal2binary(a))
            a-=1
            time.sleep(((period/2/254)))
except ArithmeticError:
    period=None

finally:
    zero = [0,0,0,0,0,0,0,0]
    GPIO.output(dac,zero)
    GPIO.cleanup()