import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

p=GPIO.PWM(22,100)
p2 = GPIO.PWM(24,100)

p.start(0)
p2.start(0)
try:
    while True:
        
        a = float(input())
        p.start((a))
        p2.start((a))

except ArithmeticError:
    a = None
finally:
    GPIO.output(24,0)
    GPIO.output(22,0)
    GPIO.cleanup()