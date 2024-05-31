from machine import Pin
import time

touch_pin = Pin(32, Pin.IN)

while True:
    if touch_pin.value() == 1:
        print("Touch!")
    else:
        print("...")
    time.sleep(0.5)
