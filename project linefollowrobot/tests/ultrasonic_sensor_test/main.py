header_H = 0x55  # Header
header_L = 0xAA  # Header
device_Addr = 0x11  # Address
data_Length = 0x00  # Data length
get_Dis_CMD = 0x02  # Command: Read Distance
checksum = header_H + header_L + device_Addr + data_Length + get_Dis_CMD  # Checksum

i = 0
Distance = 0
Rx_DATA = bytearray(8)
CMD = bytearray([
    header_H, header_L, device_Addr, data_Length, get_Dis_CMD, checksum
])  # Distance command package

from machine import UART, Pin
from time import sleep

uart = UART(1, 19200, tx=17, rx=16)
ir_sens = Pin(15, Pin.OUT)

led = Pin(15, Pin.IN)
led_state = 0



while True:
    uart.write(CMD)
    
    sleep(0.150)
    
    led_state = not led_state
    led.value(led_state)
    
    while uart.any() > 0:
        msg = uart.read()
        Distance=((msg[5]<<8)|msg[6])
        
        print(f"{Distance} cm")
    print(ir_sens.value())