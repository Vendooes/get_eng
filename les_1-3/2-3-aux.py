import RPi.GPIO as GPIO
import time
leds = [9,10,22,27,17,4,3,2] 
aux = [21,20,26,16,19,25,23,24]
GPIO.setmode(GPIO.BCM)
for i in leds:
    GPIO.setup(i,GPIO.OUT)
    GPIO.output(i,1)
for q in aux:
    GPIO.setup(q,GPIO.IN)
while True:
    for q in range(8):
        GPIO.output(leds[q],GPIO.input(aux[q]))
GPIO.cleanup()

