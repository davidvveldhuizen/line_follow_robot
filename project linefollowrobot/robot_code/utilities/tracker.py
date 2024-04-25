from machine import Pin, ADC

class Tracker:
    def __init__(self, pins = []):
        
        self.pins = [ADC(pin) for pin in pins]
    
    def read_values(self):
        values = []
        for pin in self.pins:
            value = pin.read()
            values.append(value)
            
        return values
    
if __name__ == "__main__":
    from time import sleep
    
    tracker = Tracker([34,35,32,33,25])
    
    while True:
        print(tracker.read_values())
        sleep(0.1)