from machine import Pin
from time import sleep

mgnt_pin = Pin(13, Pin.OUT)
led_pin = Pin(2,Pin.OUT)

while True:
    mgnt_pin.value(0)
    led_pin.value(0)
    print('on')
    sleep(5)
    
    mgnt_pin.value(1)
    led_pin.value(1)
    print('off')
    sleep(2)