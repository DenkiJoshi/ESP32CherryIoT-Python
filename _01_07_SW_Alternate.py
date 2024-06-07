from machine import Pin
import time

sw_pin = Pin(32, Pin.IN)
flag = False

while True:
    state = sw_pin.value()
    if state == 0:  # If the switch is pressed, "LOW"
        flag = not flag
        time.sleep(0.2)  # Debounce delay

    if flag:
        print("ON")
    else:
        print("OFF")
    
    time.sleep(0.5)
