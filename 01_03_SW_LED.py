from machine import Pin
import time

sw = Pin(32, Pin.IN)
led = Pin(25, Pin.OUT)

while True:
    state = sw.value()
    if state == 1:
        led.value(1)  # LED on
        print("Pushed")
    else:
        led.value(0)  # LED off
        print("Not Pushed")
    
    time.sleep(0.2)