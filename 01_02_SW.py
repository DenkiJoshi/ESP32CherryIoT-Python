from machine import Pin
import time

sw = Pin(32, Pin.IN)

while True:
    state = sw.value()  # Check switch status. If pushed, "1"
    if state == 1:
        print("Pushed")
    else:
        print("Not Pushed")
    
    time.sleep(1)