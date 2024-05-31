from machine import Pin
import time

led = Pin(25, Pin.OUT)

for i in range(10):
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)