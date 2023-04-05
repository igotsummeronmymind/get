import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

GPIO.setup(troyka, GPIO.OUT, initial=1)
GPIO.setup(comp, GPIO.IN)

def dectobin(value):
    return [int(elem) for elem in bin(value)[2:].zfill(8)]

def adc():
    for i in range(256):
        x = dectobin(i)
        GPIO.output(dac, x)
        time.sleep(0.001)
        if GPIO.input(comp) == 0:
            GPIO.output(dac, 0)
            return i


try:
    while (True):
        print(adc() * 3.3 / 256)


finally:
    for i in dac:
        GPIO.output(dac, 0)
    GPIO.cleanup()
