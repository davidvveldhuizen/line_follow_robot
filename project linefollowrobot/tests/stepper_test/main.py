from time import sleep_us, sleep, time_ns, time

from machine import Pin, PWM

#hi

def toggle_led():
    global led_state
    led_state = not led_state
    led_pin.value(led_state)

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Stepper:
    def __init__(self, step, dir):
        self.freq = 800
        self.target_freq = -3200
        
        self.step_pin = PWM(Pin(step), duty_u16=30000, freq=self.freq)
        self.dir_pin = Pin(dir, Pin.OUT)
        
        self.dir = 0
        self.dir_pin.value(0)
        
        
        self.max_acc = 2
        
        self.prev_time = time_ns()
    
    def set_freq(self, freq):
        self.target_freq = freq
        
    def get_step_dir(self, freq):
        step = abs(freq)
        if step is 0:
            step = 1
        
        dir = (sign(freq) + 1)/2
        
        return step, dir
        
    
    def update(self):
        time = time_ns()
        dt = int((time - self.prev_time) / 1_000) / 1_000
        
        if self.target_freq is not self.freq:
            self.stear_speed(dt)
            
            #print(f"{self.freq} - {self.step_pin.freq()} -- {self.dir_pin.value()}")
        
        self.prev_time = time
    
    def stear_speed(self, dt):
        acc_dir = sign(self.target_freq - self.freq)
        acc = int(acc_dir * self.max_acc * dt)
        
        #print(acc)
        print(dt)
        self.freq += acc
        #print(self.freq)
        
        step, dir = self.get_step_dir(self.freq)
        
        self.step_pin.freq(step)
        self.dir_pin.value(dir)
        
sleep(1)
            
stepper1 = Stepper(step = 33,dir = 25)
#stepper2 = Stepper(step = 26,dir = 27)
#stepper2.dir_pin.value(1)

led_pin = Pin(2, Pin.OUT)
led_state = 0

print('start')

step = Pin(33, Pin.OUT)

while True:
    pass
    #stepper1.update()
    #stepper2.update()
    
#     if stepper1.freq >= 3200:
#         stepper1.target_freq = -3200
#         print("going back")
#     if stepper1.freq <= -3200:
#         stepper1.target_freq = 3200
#         print("going straight")
        
    #sleep_us(20000)
