from machine import Pin
import time

motor_pin = Pin(25, Pin.OUT)

while True:
    motor_pin.on()
    time.sleep(1)
    motor_pin.off()
    time.sleep(3)
