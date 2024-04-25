from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
count = 0

while True:
    led.value(not led.value())
    sleep(0.5)
    print(count)
    count += 1