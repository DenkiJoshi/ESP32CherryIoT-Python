from machine import Pin
import time

rupt_pin = Pin(32, Pin.IN)

while True:
    if rupt_pin.value() == 0:
        print("Interrupt!")
    else:
        print("...")
    time.sleep(0.5)
