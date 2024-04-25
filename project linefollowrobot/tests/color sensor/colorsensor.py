from machine import I2C, Pin, PWM
from time import sleep
from tcs34725 import TCS34725

i2c = I2C(0, scl=Pin(22, Pin.OUT), sda=Pin(21, Pin.OUT), freq=400000)
print(i2c.scan())
tcs = TCS34725(i2c)



def html_rgb(data):
    r, g, b, c = data
    red = int(pow((int((r/c) * 256) / 255), 2.5) * 255)
    green = int(pow((int((g/c) * 256) / 255), 2.5) * 255)
    blue = int(pow((int((b/c) * 256) / 255), 2.5) * 255)
    return red, green, blue

while 1:
    print(html_rgb(tcs.read(raw=True)))
    
    
    sleep(0.3)
    
    

