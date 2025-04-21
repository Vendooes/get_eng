import RPi.GPIO as GPIO
dac = [8,11,7,1,0,5,12,6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
def decimal2binary(val):
    return [int(el) for el in bin(val)[2:].zfill(8)]
GPIO.output(dac,0)
try:
    while True:
        a = input()
        if a == 'q':
            break
        try:
            value = int(a)
            if value<0:
                print('a меньше 0')
            elif value>255:
                print('a больше разрешенного числа')
            else:
                zel = decimal2binary(int(a))
                for p in range(len(zel)):
                    GPIO.output(dac[p],zel[p])
                print('Напряжение' ,int(a)/255*3.3,'V')
        except ValueError:
            print('Введено не целое число или не число')

finally:
    zero = [0,0,0,0,0,0,0,0]
    GPIO.output(dac,zero)
    GPIO.cleanup()