from machine import Pin
import time

vib_pin = Pin(25, Pin.OUT)

while True:
    vib_pin.on()
    time.sleep(1)
    vib_pin.off()
    time.sleep(1)
