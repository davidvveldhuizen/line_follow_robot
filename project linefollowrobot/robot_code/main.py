from tracker import Tracker
from time import sleep


tracker = Tracker([34,35,32,33,25])

while 1:
    print(tracker.read_values())
    sleep(0.1)