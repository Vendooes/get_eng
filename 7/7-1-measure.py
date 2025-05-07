import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

#Объявляем все переменные и делаем настройку GPIO
dac = [6,12,5,0,1,7,11,8]
leds = [9,10,22,27,17,4,3,2]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

#Пишем функцию для перевода в двоичную систему счисления
def decima(value):
    return[int(element) for element in bin(value)[2:].zfill(8)]

#Пишем быстрый АЦП 
def adc1():
    value = 0
    for i in range(8):
        value+=2**(7-i)
        GPIO.output(dac,decima(value))
        time.sleep(0.001)
        if GPIO.input(comp)==1:
            value-=2**(7-i)
    return value

#Делаем отображения напряжения при помощи светодиодов на leds
def bin_leds():
    
        dv=adc1()/0.012890625
        if dv<28:
            GPIO.output(leds, [0]*8)
        elif dv<57:
            GPIO.output(leds, [0, 0, 0, 0, 0, 0, 0, 1])
        elif dv<85:
            GPIO.output(leds, [0, 0, 0, 0, 0, 0, 1, 1])
        elif dv<114:
            GPIO.output(leds, [0, 0, 0, 0, 0, 1, 1, 1])
        elif dv<142:
            GPIO.output(leds, [0, 0, 0, 0, 1, 1, 1, 1])
        elif dv<171:
            GPIO.output(leds, [0, 0, 0, 1, 1, 1, 1, 1])
        elif dv<199:
            GPIO.output(leds, [0, 0, 1, 1, 1, 1, 1, 1])
        elif dv<228:
            GPIO.output(leds, [0, 1, 1, 1, 1, 1, 1, 1])
        else:
            GPIO.output(leds, [1, 1, 1, 1, 1, 1, 1, 1])

#Основной блок 
try:
    values = []
    time_start = time.time()
    GPIO.output(troyka, GPIO.HIGH)

    print("Идет заряд")
    while adc1() < 200:
        values.append(adc1())

    print("Идет разряд")
    GPIO.output(troyka, GPIO.LOW)

    while adc1() > 100:
        values.append(adc1())

    time_stop = time.time()
    dr = time_stop - time_start

    plt.plot(values)
    plt.show()
    values_str = [str(i) for i in values]
    with open("data.txt", "w") as f:
        f.write("\n".join(values_str))

    Time = dr/len(values)
    n = 1/Time
    qs = 3.3/256
    with open("settings.txt", "w") as out:
        out.write(f"n = {n}, qs = {qs}, T = {Time}, dr = {dr}")
        print(f'Общая продолжительность эксперимента - {round(Time, 4)} c, \nпериод одного измерения - {round(Time/len(values), 5)} c,\nсредняя частота дискретизации проведённых измерений - {round(1/Time*len(values), 3)} Гц\nшаг квантования АЦП - {round(3.3/256, 5)} В')

except KeyboardInterrupt:
    print('Программа остановлена')
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()