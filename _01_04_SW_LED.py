from machine import Pin
import time

sw_pin = Pin(32, Pin.IN)
led_pin = Pin(25, Pin.OUT)

while True:
    state = sw_pin.value()
    if state == 1:
        led_pin.value(1)  # LED on
        print("Pushed")
    else:
        led_pin.value(0)  # LED off
        print("Not Pushed")
    
    time.sleep(0.2)