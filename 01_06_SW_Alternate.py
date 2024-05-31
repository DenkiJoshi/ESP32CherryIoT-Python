from machine import Pin
import time

sw = Pin(32, Pin.IN)
flag = False
prev_state = False

while True:
    state = sw.value()  # Check switch status. If pushed, "1"
    if state != prev_state:
        if state == False:
            flag = not flag
            if flag:
                print("ON")
            else:
                print("OFF")
    prev_state = state
    time.sleep(0.1) 
