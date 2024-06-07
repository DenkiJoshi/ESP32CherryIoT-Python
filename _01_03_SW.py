from machine import Pin
import time

sw_pin = Pin(32, Pin.IN)

while True:
    state = sw_pin.value()  # Check switch status. If pushed, "1"
    if state == 1:
        print("Pushed")
    else:
        print("Not Pushed")
    
    time.sleep(1)