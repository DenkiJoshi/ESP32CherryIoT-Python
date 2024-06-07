from machine import Pin
import time

led_pin = Pin(25, Pin.OUT)

while True:
    led_pin.on()  # LED on
    time.sleep(0.1)  # sec (1000msec=1sec)
    led_pin.off()  # LED off
    time.sleep(0.1)
    led_pin.on()
    time.sleep(0.1)
    led_pin.off()
    time.sleep(0.1)
    led_pin.on()
    time.sleep(1)
    led_pin.off()
    time.sleep(1)
