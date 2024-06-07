from machine import Pin, PWM
import time

led_pin = Pin(25, Pin.OUT)
pwm = PWM(led_pin)

while True:
    for i in range(256):  # Increase the brightness from 0 to 255
        pwm.duty(i)
        time.sleep_ms(10)  # Change speed
    for i in range(255, -1, -1):  # Decrease the brightness from 255 to 0
        pwm.duty(i)
        time.sleep_ms(10)  # Change speed