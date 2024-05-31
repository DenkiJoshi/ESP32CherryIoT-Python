from machine import Pin, PWM
import time

led = Pin(25, Pin.OUT)

while True:
    for i in range(3):
        led.on()  # LED on
        time.sleep(0.5)
        led.off()  # LED off
        time.sleep(0.5)
    time.sleep(2)