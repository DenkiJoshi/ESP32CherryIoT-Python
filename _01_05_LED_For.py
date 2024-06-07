from machine import Pin, PWM
import time

led_pin = Pin(25, Pin.OUT)

while True:
    for i in range(3):
        led_pin.on()  # LED on
        time.sleep(0.5)
        led_pin.off()  # LED off
        time.sleep(0.5)
    time.sleep(2)