from machine import Pin
import time

led_pin = Pin(25, Pin.OUT)

for i in range(10):
    led_pin.value(1)
    time.sleep(1)
    led_pin.value(0)
    time.sleep(1)