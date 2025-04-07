import RPi.GPIO as GPIO
import time 
leds = [2,3,4,17,27,22,10,9]
GPIO.setmode(GPIO.BCM)
for i in leds:
    GPIO.setup(i,GPIO.OUT)
for _ in range(3):
    for i in leds:
        GPIO.output(i,1)
        time.sleep(0.2)
        GPIO.output(i,0)
GPIO.output(all_pins,0)
GPIO.cleanup()