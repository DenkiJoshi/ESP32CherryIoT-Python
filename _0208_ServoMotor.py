from machine import Pin, PWM
import time

class Servo:
    def __init__(self, pin):
        self.pin = pin
        self.pwm = PWM(Pin(pin), freq=50)
        self.min_pulse_width_us = 500  # Default minimum pulse width for 0 degrees）
        self.max_pulse_width_us = 2500  # Default maximum pulse width for 180 degrees
        self.period_hertz = 50  # Default PWM frequency

    def write_angle(self, angle):
        # Convert angle to pulse width
        pulse_width_us = self.min_pulse_width_us + (self.max_pulse_width_us - self.min_pulse_width_us) * angle / 180
        # Set pulse width
        self.pwm.duty(int(pulse_width_us / 20))  # Set duty cycle in 20μs units

    def set_period_hertz(self, hertz):
        # Set PWM frequency
        self.period_hertz = hertz
        self.pwm.freq(hertz)

servo = Servo(pin=3)

while True:
    for angle in range(0, 181): # 0-180 right
        servo.write_angle(angle)
        time.sleep_ms(15)

    for angle in range(180, -1, -1): # 180-0  left
        servo.write_angle(angle)
        time.sleep_ms(15)
